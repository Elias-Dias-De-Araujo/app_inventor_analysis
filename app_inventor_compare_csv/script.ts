import { readFile, readdir } from 'fs/promises'

const folderName = 'fdr_projects'
const solutionFileName = 'total.csv'

type QuestionItem = {
    name: string
    value: number
}

type Question = {
    name: string
    items: QuestionItem[]
}

type SubmissionItem = {
    name: string
    questions: QuestionItem[]
}

type Submission = {
    name: string
    items: SubmissionItem[]
}

type DifferItem = {
    differ: number
} & Omit<QuestionItem, 'value'>

type Differ = {
    /** Soma de todos os differs da submissão */
    score: number

    items: DifferItem[]
}

const readQuestion = (content: string): QuestionItem[] => {
    const lines = content.split(/\r\\|\n|\r/).filter((x) => x)

    return lines.map((x) => {
        const [name, value] = x.split(',')

        return {
            name,
            value: parseInt(value),
        }
    })
}

// Pega os itens da pasta `projects` e separa em `questions` e `submissions`
const getItems = async () => {
    const items = await readdir(folderName)

    const questions = items.filter((x) => x.endsWith('.csv'))

    const submissions = items.filter((x) => !x.endsWith('.csv'))

    return {
        questions,
        submissions,
    }
}

// Reune os dados de cada questão e submissão
const dataset = async (questions: string[], submissions: string[]) => {
    const questionsPromise = async () => {
        const questionsMatchers: Question[] = []
        for await (const question of questions) {
            const questionRaw = await readFile(
                `${folderName}/${question}`,
                'utf-8'
            )

            questionsMatchers.push({
                name: question,
                items: readQuestion(questionRaw),
            })
        }

        return questionsMatchers
    }

    const submissionsPromise = async () => {
        const submissionsMatches: Submission[] = []
        for await (const submission of submissions) {
            const solutions = await readdir(`${folderName}/${submission}`).then(
                (x) =>
                    x.filter(
                        (x) => !x.match(/\.csv|\.aia|.zip|\.apk|\.mp4|\.docx$/)
                    )
            )

            const items: SubmissionItem[] = await Promise.all(
                solutions.map(async (sol) => {
                    const total = await readFile(
                        `${folderName}/${submission}/${sol}/${solutionFileName}`,
                        'utf-8'
                    )

                    return {
                        name: sol,
                        questions: readQuestion(total),
                    }
                })
            )

            submissionsMatches.push({
                name: submission,
                items,
            })
        }

        return submissionsMatches
    }

    const [questionsData, submissionsData] = await Promise.all([
        questionsPromise(),
        submissionsPromise(),
    ])

    return {
        questionsData,
        submissionsData,
    }
}

// Retorna um objeto com as diferenças entre duas questões
const differ = (left: QuestionItem[], right: QuestionItem[]): Differ => {
    const items: DifferItem[] = []
    for (const leftItem of left) {
        for (const rightItem of right) {
            if (leftItem.name === rightItem.name) {
                const item: DifferItem = {
                    name: leftItem.name,
                    differ: leftItem.value - rightItem.value,
                }

                items.push(item)
            }
        }
    }

    return {
        items,
        score: items.reduce((acc, curr) => acc + curr.differ, 0),
    }
}

const bootstrapExec = async () => {
    // lê o nome de todas as pastas na pasta fdr_projects
    const { questions, submissions } = await getItems()

    const { questionsData, submissionsData } = await dataset(
        questions,
        submissions
    )

    return {
        questionsData,
        submissionsData,
        questions,
        submissions,
    }
}

async function main() {
    const bootstrap = await bootstrapExec()

    const result = Object.fromEntries(
        bootstrap.questions.map((x) => {
            return [x, [] as Submission[]]
        })
    )

    // console.log(bootstrap.submissionsData)

    for (const question of bootstrap.questionsData) {
        for (const submission of bootstrap.submissionsData) {
            let founded = false

            for (const item of submission.items) {
                const diff = differ(item.questions, question.items)

                if (diff.items.every((x) => x.differ >= 0)) {
                    founded = true
                    break
                }
            }

            if (founded) {
                result[question.name].push(submission)
            }
        }
    }

    const resultSubmissions = Object.fromEntries(
        bootstrap.submissions.map((x) => {
            return [x, [] as string[]]
        })
    )

    for (const submission of bootstrap.submissions) {
        for (const question of bootstrap.questions) {
            const subs = result[question]

            if (subs.some((x) => x.name === submission)) {
                resultSubmissions[submission].push(question.split('.')[0])
            }
        }
    }

    const countQ = Object.entries(Object.entries(result).map(([question, submissions]) => {
        return [question, submissions.length]
    }))

    console.log(countQ)

    console.log(resultSubmissions)

    const length = 3
    var countQOnly = Array.from({ length }, () => 0);

    // Loop atrávez das chaves no data object
    for (const key in resultSubmissions) {
        if (resultSubmissions[key].length === 1 && resultSubmissions[key][0] === 'Q1') {
            countQOnly[0]++
        }else if(resultSubmissions[key].length === 1 && resultSubmissions[key][0] === 'Q2') {
            countQOnly[1]++
        }else if(resultSubmissions[key].length === 1 && resultSubmissions[key][0] === 'Q3') {
            countQOnly[2]++
        }
    }
    // for (let index = 0; index < countQOnly.length; index++) {
    //     //console.log(`Q${index+1}: ${countQOnly[index]}`)
    // }
}

main()