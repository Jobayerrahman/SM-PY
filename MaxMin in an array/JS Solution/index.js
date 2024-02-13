let questionArray = [62,75,57,2,15]

question  = document.getElementById('question')
result01  = document.getElementById('result01')
result02  = document.getElementById('result02')

function maxElement(array){
    maxElement = array[0]
    for(i=0; i<array.length; i++){
        if(maxElement < array[i]){
            maxElement = array[i]
        }
    }
    return maxElement
}

function minElement(array){
    minElement = array[0]
    for(i=0; i<array.length; i++){
        if(minElement > array[i]){
            minElement = array[i]
        }
    }
    return minElement
}



//OutPut Area
question.innerHTML= "[ " + questionArray +" ]"
result01.innerHTML= "Max element in array : " + maxElement(questionArray) +"."
result02.innerHTML= "Min element in array : " + minElement(questionArray) +"."