import xml.etree.ElementTree as ET

xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<xml xmlns="http://www.w3.org/1999/xhtml">
   <block type="lists_create_with" id="/qpyrWk(wzP0?JRzdlT}" x="-113" y="-266">
      <mutation items="1" />
      <value name="ADD0">
         <block type="text" id="{)Gxj3J0V+B)Zk|B%f78">
            <field name="TEXT">Item</field>
         </block>
      </value>
   </block>
   <block type="lists_create_with" id="1f$bljyd|oJ7GB6(58x0" x="-110" y="-208">
      <mutation items="1" />
      <value name="ADD0">
         <block type="text" id="Y2I}Xi5N;CEgeBOkb@m2">
            <field name="TEXT">Item</field>
         </block>
      </value>
   </block>
   <block type="component_event" id="104" x="458" y="-208">
      <mutation component_type="ImageSprite" is_generic="false" instance_name="ImageSprite1" event_name="Dragged" />
      <field name="COMPONENT_SELECTOR">ImageSprite1</field>
      <statement name="DO">
         <block type="component_method" id="105" inline="false">
            <mutation component_type="ImageSprite" method_name="MoveTo" is_generic="false" instance_name="ImageSprite1" />
            <field name="COMPONENT_SELECTOR">ImageSprite1</field>
            <value name="ARG0">
               <block type="lexical_variable_get" id="106">
                  <mutation>
                     <eventparam name="currentX" />
                  </mutation>
                  <field name="VAR">currentX</field>
               </block>
            </value>
            <value name="ARG1">
               <block type="component_set_get" id="107">
                  <mutation component_type="ImageSprite" set_or_get="get" property_name="Y" is_generic="false" instance_name="ImageSprite1" />
                  <field name="COMPONENT_SELECTOR">ImageSprite1</field>
                  <field name="PROP">Y</field>
               </block>
            </value>
         </block>
      </statement>
   </block>
   <block type="lists_create_with" id="=#W+r$Ae+%;-)9dCusV7" x="-105" y="-161">
      <mutation items="1" />
      <value name="ADD0">
         <block type="text" id="[xLE;u*R=FRZ2__Vum,$">
            <field name="TEXT">Item</field>
         </block>
      </value>
   </block>
   <block type="global_declaration" id="92" inline="false" x="-113" y="-108">
      <field name="NAME">score</field>
      <value name="VALUE">
         <block type="math_number" id="93">
            <field name="NUM">0</field>
         </block>
      </value>
   </block>
   <block type="component_event" id="74" x="-159" y="-54">
      <mutation component_type="Button" is_generic="false" instance_name="ButtonStart" event_name="Click" />
      <field name="COMPONENT_SELECTOR">ButtonStart</field>
      <statement name="DO">
         <block type="component_method" id="75" inline="false">
            <mutation component_type="Ball" method_name="MoveTo" is_generic="false" instance_name="Ball1" />
            <field name="COMPONENT_SELECTOR">Ball1</field>
            <value name="ARG0">
               <block type="math_division" id="76">
                  <value name="A">
                     <block type="component_set_get" id="77">
                        <mutation component_type="Canvas" set_or_get="get" property_name="Width" is_generic="false" instance_name="Canvas1" />
                        <field name="COMPONENT_SELECTOR">Canvas1</field>
                        <field name="PROP">Width</field>
                     </block>
                  </value>
                  <value name="B">
                     <block type="math_number" id="78">
                        <field name="NUM">2</field>
                     </block>
                  </value>
               </block>
            </value>
            <value name="ARG1">
               <block type="math_number" id="79">
                  <field name="NUM">0</field>
               </block>
            </value>
            <next>
               <block type="component_set_get" id="80" inline="false">
                  <mutation component_type="Ball" set_or_get="set" property_name="Enabled" is_generic="false" instance_name="Ball1" />
                  <field name="COMPONENT_SELECTOR">Ball1</field>
                  <field name="PROP">Enabled</field>
                  <value name="VALUE">
                     <block type="logic_boolean" id="81">
                        <field name="BOOL">TRUE</field>
                     </block>
                  </value>
                  <next>
                     <block type="component_set_get" id="82" inline="false">
                        <mutation component_type="Ball" set_or_get="set" property_name="Heading" is_generic="false" instance_name="Ball1" />
                        <field name="COMPONENT_SELECTOR">Ball1</field>
                        <field name="PROP">Heading</field>
                        <value name="VALUE">
                           <block type="math_random_int" id="83">
                              <value name="FROM">
                                 <block type="math_number" id="84">
                                    <field name="NUM">225</field>
                                 </block>
                              </value>
                              <value name="TO">
                                 <block type="math_number" id="85">
                                    <field name="NUM">315</field>
                                 </block>
                              </value>
                           </block>
                        </value>
                        <next>
                           <block type="component_set_get" id="86" inline="false">
                              <mutation component_type="Ball" set_or_get="set" property_name="Speed" is_generic="false" instance_name="Ball1" />
                              <field name="COMPONENT_SELECTOR">Ball1</field>
                              <field name="PROP">Speed</field>
                              <value name="VALUE">
                                 <block type="math_number" id="87">
                                    <field name="NUM">5</field>
                                 </block>
                              </value>
                              <next>
                                 <block type="component_set_get" id="88" inline="false">
                                    <mutation component_type="Ball" set_or_get="set" property_name="Interval" is_generic="false" instance_name="Ball1" />
                                    <field name="COMPONENT_SELECTOR">Ball1</field>
                                    <field name="PROP">Interval</field>
                                    <value name="VALUE">
                                       <block type="math_number" id="89">
                                          <field name="NUM">10</field>
                                       </block>
                                    </value>
                                    <next>
                                       <block type="procedures_callnoreturn" id="90" inline="false">
                                          <mutation name="changeAndShowScore">
                                             <arg name="newScore" />
                                          </mutation>
                                          <field name="PROCNAME">changeAndShowScore</field>
                                          <value name="ARG0">
                                             <block type="math_number" id="91">
                                                <field name="NUM">0</field>
                                             </block>
                                          </value>
                                       </block>
                                    </next>
                                 </block>
                              </next>
                           </block>
                        </next>
                     </block>
                  </next>
               </block>
            </next>
         </block>
      </statement>
   </block>
   <block type="component_event" id="94" x="459" y="-23">
      <mutation component_type="Button" is_generic="false" instance_name="ButtonReset" event_name="Click" />
      <field name="COMPONENT_SELECTOR">ButtonReset</field>
      <statement name="DO">
         <block type="component_method" id="95" inline="false">
            <mutation component_type="Ball" method_name="MoveTo" is_generic="false" instance_name="Ball1" />
            <field name="COMPONENT_SELECTOR">Ball1</field>
            <value name="ARG0">
               <block type="math_division" id="96">
                  <value name="A">
                     <block type="component_set_get" id="97">
                        <mutation component_type="Canvas" set_or_get="get" property_name="Width" is_generic="false" instance_name="Canvas1" />
                        <field name="COMPONENT_SELECTOR">Canvas1</field>
                        <field name="PROP">Width</field>
                     </block>
                  </value>
                  <value name="B">
                     <block type="math_number" id="98">
                        <field name="NUM">2</field>
                     </block>
                  </value>
               </block>
            </value>
            <value name="ARG1">
               <block type="math_number" id="99">
                  <field name="NUM">0</field>
               </block>
            </value>
            <next>
               <block type="component_set_get" id="100" inline="false">
                  <mutation component_type="Ball" set_or_get="set" property_name="Enabled" is_generic="false" instance_name="Ball1" />
                  <field name="COMPONENT_SELECTOR">Ball1</field>
                  <field name="PROP">Enabled</field>
                  <value name="VALUE">
                     <block type="logic_boolean" id="101">
                        <field name="BOOL">FALSE</field>
                     </block>
                  </value>
                  <next>
                     <block type="procedures_callnoreturn" id="102" inline="false">
                        <mutation name="changeAndShowScore">
                           <arg name="newScore" />
                        </mutation>
                        <field name="PROCNAME">changeAndShowScore</field>
                        <value name="ARG0">
                           <block type="math_number" id="103">
                              <field name="NUM">0</field>
                           </block>
                        </value>
                     </block>
                  </next>
               </block>
            </next>
         </block>
      </statement>
   </block>
   <block type="procedures_defnoreturn" id="108" x="321" y="187">
      <mutation>
         <arg name="newScore" />
      </mutation>
      <field name="NAME">changeAndShowScore</field>
      <field name="VAR0">newScore</field>
      <statement name="STACK">
         <block type="lexical_variable_set" id="109" inline="false">
            <field name="VAR">global score</field>
            <value name="VALUE">
               <block type="lexical_variable_get" id="110">
                  <field name="VAR">newScore</field>
               </block>
            </value>
            <next>
               <block type="component_set_get" id="111" inline="false">
                  <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="LabelScore" />
                  <field name="COMPONENT_SELECTOR">LabelScore</field>
                  <field name="PROP">Text</field>
                  <value name="VALUE">
                     <block type="text_join" id="112" inline="false">
                        <mutation items="2" />
                        <value name="ADD0">
                           <block type="text" id="113">
                              <field name="TEXT">Score:</field>
                           </block>
                        </value>
                        <value name="ADD1">
                           <block type="lexical_variable_get" id="114">
                              <field name="VAR">global score</field>
                           </block>
                        </value>
                     </block>
                  </value>
               </block>
            </next>
         </block>
      </statement>
   </block>
   <block type="component_event" id="126" x="-157" y="293">
      <mutation component_type="Ball" is_generic="false" instance_name="Ball1" event_name="EdgeReached" />
      <field name="COMPONENT_SELECTOR">Ball1</field>
      <statement name="DO">
         <block type="controls_if" id="127" inline="false">
            <mutation else="1" />
            <comment pinned="false" h="49" w="148">-1 signifies the bottom edge.</comment>
            <value name="IF0">
               <block type="math_compare" id="128">
                  <field name="OP">EQ</field>
                  <value name="A">
                     <block type="lexical_variable_get" id="129">
                        <mutation>
                           <eventparam name="edge" />
                        </mutation>
                        <field name="VAR">edge</field>
                     </block>
                  </value>
                  <value name="B">
                     <block type="math_number" id="130">
                        <field name="NUM">-1</field>
                     </block>
                  </value>
               </block>
            </value>
            <statement name="DO0">
               <block type="component_set_get" id="131" inline="false">
                  <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="LabelScore" />
                  <field name="COMPONENT_SELECTOR">LabelScore</field>
                  <field name="PROP">Text</field>
                  <value name="VALUE">
                     <block type="text" id="132">
                        <field name="TEXT">Game Over</field>
                     </block>
                  </value>
                  <next>
                     <block type="component_set_get" id="133" inline="false">
                        <mutation component_type="Ball" set_or_get="set" property_name="Enabled" is_generic="false" instance_name="Ball1" />
                        <field name="COMPONENT_SELECTOR">Ball1</field>
                        <field name="PROP">Enabled</field>
                        <value name="VALUE">
                           <block type="logic_boolean" id="134">
                              <field name="BOOL">FALSE</field>
                           </block>
                        </value>
                        <next>
                           <block type="procedures_callnoreturn" id="135" inline="false">
                              <mutation name="playSound">
                                 <arg name="source" />
                              </mutation>
                              <field name="PROCNAME">playSound</field>
                              <value name="ARG0">
                                 <block type="text" id="136">
                                    <field name="TEXT">Buzzer.mp3</field>
                                 </block>
                              </value>
                           </block>
                        </next>
                     </block>
                  </next>
               </block>
            </statement>
            <statement name="ELSE">
               <block type="component_method" id="137" inline="false">
                  <mutation component_type="Ball" method_name="Bounce" is_generic="false" instance_name="Ball1" />
                  <field name="COMPONENT_SELECTOR">Ball1</field>
                  <value name="ARG0">
                     <block type="lexical_variable_get" id="138">
                        <mutation>
                           <eventparam name="edge" />
                        </mutation>
                        <field name="VAR">edge</field>
                     </block>
                  </value>
                  <next>
                     <block type="procedures_callnoreturn" id="139" inline="false">
                        <mutation name="playSound">
                           <arg name="source" />
                        </mutation>
                        <field name="PROCNAME">playSound</field>
                        <value name="ARG0">
                           <block type="text" id="140">
                              <field name="TEXT">Note.wav</field>
                           </block>
                        </value>
                     </block>
                  </next>
               </block>
            </statement>
         </block>
      </statement>
   </block>
   <block type="component_event" id="115" x="326" y="318">
      <mutation component_type="Ball" is_generic="false" instance_name="Ball1" event_name="CollidedWith" />
      <field name="COMPONENT_SELECTOR">Ball1</field>
      <statement name="DO">
         <block type="component_set_get" id="116" inline="false">
            <mutation component_type="Ball" set_or_get="set" property_name="Heading" is_generic="false" instance_name="Ball1" />
            <field name="COMPONENT_SELECTOR">Ball1</field>
            <field name="PROP">Heading</field>
            <value name="VALUE">
               <block type="math_subtract" id="117">
                  <value name="A">
                     <block type="math_number" id="118">
                        <field name="NUM">360</field>
                     </block>
                  </value>
                  <value name="B">
                     <block type="component_set_get" id="119">
                        <mutation component_type="Ball" set_or_get="get" property_name="Heading" is_generic="false" instance_name="Ball1" />
                        <field name="COMPONENT_SELECTOR">Ball1</field>
                        <field name="PROP">Heading</field>
                     </block>
                  </value>
               </block>
            </value>
            <next>
               <block type="procedures_callnoreturn" id="120" inline="false">
                  <mutation name="changeAndShowScore">
                     <arg name="newScore" />
                  </mutation>
                  <field name="PROCNAME">changeAndShowScore</field>
                  <value name="ARG0">
                     <block type="math_add" id="121">
                        <mutation items="2" />
                        <value name="NUM0">
                           <block type="lexical_variable_get" id="122">
                              <field name="VAR">global score</field>
                           </block>
                        </value>
                        <value name="NUM1">
                           <block type="math_number" id="123">
                              <field name="NUM">1</field>
                           </block>
                        </value>
                     </block>
                  </value>
                  <next>
                     <block type="procedures_callnoreturn" id="124" inline="false">
                        <mutation name="playSound">
                           <arg name="source" />
                        </mutation>
                        <field name="PROCNAME">playSound</field>
                        <value name="ARG0">
                           <block type="text" id="125">
                              <field name="TEXT">Noink.mp3</field>
                           </block>
                        </value>
                     </block>
                  </next>
               </block>
            </next>
         </block>
      </statement>
   </block>
   <block type="procedures_defnoreturn" id="141" x="322" y="556">
      <mutation>
         <arg name="source" />
      </mutation>
      <field name="NAME">playSound</field>
      <field name="VAR0">source</field>
      <statement name="STACK">
         <block type="controls_if" id="142" inline="false">
            <value name="IF0">
               <block type="component_set_get" id="143">
                  <mutation component_type="CheckBox" set_or_get="get" property_name="Checked" is_generic="false" instance_name="SoundOnCheckBox" />
                  <field name="COMPONENT_SELECTOR">SoundOnCheckBox</field>
                  <field name="PROP">Checked</field>
               </block>
            </value>
            <statement name="DO0">
               <block type="component_set_get" id="144" inline="false">
                  <mutation component_type="Sound" set_or_get="set" property_name="Source" is_generic="false" instance_name="Sound1" />
                  <field name="COMPONENT_SELECTOR">Sound1</field>
                  <field name="PROP">Source</field>
                  <value name="VALUE">
                     <block type="lexical_variable_get" id="145">
                        <field name="VAR">source</field>
                     </block>
                  </value>
                  <next>
                     <block type="component_method" id="146">
                        <mutation component_type="Sound" method_name="Play" is_generic="false" instance_name="Sound1" />
                        <field name="COMPONENT_SELECTOR">Sound1</field>
                     </block>
                  </next>
               </block>
            </statement>
         </block>
      </statement>
   </block>
   <yacodeblocks ya-version="223" language-version="36" />
</xml>'''  # Paste your XML string here

root = ET.fromstring(xml_data)

block_types = [
    "lists_create_with",
    "text",
    "component_event",
    "component_method",
    "lexical_variable_get",
    "component_set_get",
    "global_declaration",
    "math_number",
    "logic_boolean",
    "procedures_callnoreturn",
    "procedures_defnoreturn",
    "lexical_variable_set",
    "text_join",
    "controls_if",
    "math_compare",
    "math_number",
    "component_method",
    "procedures_callnoreturn",
    "math_division",
    "math_subtract",
    "math_add"
]

block_type_counts = {block_type: 0 for block_type in block_types}

for block in root.findall('.//{http://www.w3.org/1999/xhtml}block'):
    block_type = block.get('type')
    if block_type in block_type_counts:
        block_type_counts[block_type] += 1

for block_type, count in block_type_counts.items():
    print(f"{block_type}: {count}")