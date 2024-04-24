import re
import pyautogui as pya

text_example = "O conteúdo do documento de Engenharia Legal deve ser {{c1::objetivo}}, {{c2::com propósito claro}}, que é {{c3::elucidar as questões elencadas pelo juiz ao perito.}}"


def convert_two_spaces_to_newline(string):
    text_split = string.split("  ")
    new_text = ""

    for k in text_split:
        new_text += k + "\n"
    
    return new_text

def seperate_dot(string):

    if "[...]" in string:
        print("question is occlusion!")
        return

    text_split = string.split(".")
    new_text = ""

    for k in text_split:
        new_text += k.strip() + "\n"
    
    return new_text.strip()

def seperate_occlusion(string):
    answers = ""
    replaced_question = string

    x = re.findall("\{\{.+?\}\}", string )

    id = 0

    if x == []: # if empty, print
        print("its empty!!")
        pya.alert("The seperate occlusion is empty!")
        raise Exception("The seperate occlusion returns a empty array!")

    for k in x:
        answers += k[6:len(k) - 2] + "\n"
        id += 1
        replaced_question = replaced_question.replace(k, "(" + str(id) + ") " + "[...]")
    
    return replaced_question, answers
    

def text_parse(text):
    new_text = seperate_occlusion(text)
    new_text = seperate_dot(text)

    return new_text

def test(file):
    try:
        found_file = open(file, "r")
    except:
        pya.alert("The file doesn't exist")
        raise Exception("The file doesn't exist!")
    
    lines = found_file.readlines()

    for line in lines:
        
        if "#" in line:
            continue

        text_found = line.split("\t")
        
        question_found = ""
        answer_found = ""

        if len(text_found) == 1:
            print("no answer!")
            question_found, answer_found = seperate_occlusion(text_found[0])
        else:
            question_found = text_found[0]
            answer_found = text_found[1]

        print(question_found)
        print(answer_found)
        
    
    found_file.close()