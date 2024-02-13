//Declaration
let questionArray = [23,45,64,13,67]
let resultArray   = []
QArray = document.getElementById("QArray")
RArray = document.getElementById("RArray")

//Operation Area
let lengthOfQuestionArray = questionArray.length - 1
for (i=lengthOfQuestionArray; i>-1; i--){resultArray.push(questionArray[i])}


//OutPut Area
QArray.innerHTML= "[ " + questionArray +" ]"
RArray.innerHTML= "[ " + resultArray +" ]"

