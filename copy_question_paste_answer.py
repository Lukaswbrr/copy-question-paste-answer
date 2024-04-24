import pyperclip
import pyautogui as pya
import time

import text_parser as tp

questions = []
answers = []

def add_question(string):
    if string == "":
        pya.alert("A question is empty!", "Fatal Error", "Close")
        raise Exception("A question is empty")
    
    questions.append(string)

def add_answer(string):
    if string == "":
        pya.alert("A question doesn't have a answer!", "Fatal Error", "Close")
        print( questions )
        raise Exception("A question doesn't have a answer")

    answers.append(string)

def read_text_file(file):
    try:
        found_file = open(file, "r")
    except:
        pya.alert("The file doesn't exist!", "Error", "Close")
        raise Exception("The file doesn't exist!")
    
    lines = found_file.readlines()

    for line in lines:
        
        if "#" in line:
            continue

        text_found = line.split("\t")
        
        question_found = ""
        answer_found = ""
        #print(len(text_found))
        #print(text_found[1])
        #print(type(text_found[1]))
        if "{{c1::" in text_found[0]:
            print("no answer!")
            question_found, answer_found = tp.seperate_occlusion(text_found[0])
            question_found = question_found.strip()
            answer_found = answer_found.strip()
        else:
            question_found = text_found[0]
            answer_found = text_found[1]

            answer_found = tp.seperate_dot(answer_found)

        add_question(question_found)
        add_answer(answer_found)
        
    
    found_file.close()

def sequence_test(index):
    pyperclip.copy(questions[index])
    time.sleep(0.5)
    pya.hotkey("ctrl", "v")
    pyperclip.copy(answers[index])
    time.sleep(0.5)
    pya.hotkey("ctrl", "v")
    pya.leftClick()


def sequence_start():
    if not len(questions) == len(answers):
        pya.alert("The file contains questions and answers that aren't the same size!", "Fatal Error", "Close")
        raise Exception("The questions and answers sizes are not the same!") # returns error if questions and answers are not same size

    try:
        for k in range(len(questions)):
            sequence_test(k)
        
        pya.alert("Sequence finished", "Alert", "Close")
    except:
        pya.alert("Sequence failed!", "Fatal Error", "Close")

prompt_text = pya.prompt("Type file name located at export folder\n\nBefore pressing OK: Set the zoom value to 10%, Point the mouse to the main topic and wait 5 seconds to start the input sequence. \n\nWhen the sequence has started, wait for it to finish.", "Enter file")

if prompt_text == None or prompt_text == "":
    print("Cancelled Operation")
else:
    read_text_file("export/" + prompt_text)
    print("Started operation")
    time.sleep(5)
    sequence_start()