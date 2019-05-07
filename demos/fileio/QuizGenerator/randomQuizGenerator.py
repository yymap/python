#! python3
'''
Random quiz generator,create quizes with question and answer in random order
'''

import random


def generateQuiz(quizTitle, contents, quizCount, questionCount) :
    # Generate 5 quiz
    for quizNum in range(quizCount) :
        quizFile = open('quiz%s.txt' % (quizNum+1), 'w')
        answerFile = open('quiz_answer%s.txt' % (quizNum+1), 'w')
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write(' '*20 + quizTitle + ' Quiz (Form %s)' % (quizNum+1) )
        quizFile.write('\n\n')

        # shuffle the order of the states
        states = list(contents.keys())
        random.shuffle(states)

        # Loop all states ,making a question for each
        for questionNum in range(questionCount) :
            correctAnswer = contents[states[questionNum]]
            wrongAnswers = list(contents.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers,3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # write qeustion file
            quizFile.write('%s, What is the capital of %s \n'  % (questionNum+1, states[questionNum]) )
            for i in range(4) :
                quizFile.write('%s. %s\n' % ('ABCD'[i],answerOptions[i]) )
            quizFile.write('\n')

            # Write answer file
            answerFile.write('%s. %s\n' % (questionNum+1,'ABCD'[answerOptions.index(correctAnswer)] ) )

        quizFile.close()
        answerFile.close()
                       
    
def testGenerateQuiz() :
    contents = {'HeBei':'ShiJiaZhuang','LiaoNing':'ShenYang','HeNan':'ZhengZhou','ShanXi':'XiAn','SiChuan':'ChengDu','JiangSu':'NanJing','ZheJiang':'HangZhou'}
    generateQuiz('State', contents, 4,3)


testGenerateQuiz()
