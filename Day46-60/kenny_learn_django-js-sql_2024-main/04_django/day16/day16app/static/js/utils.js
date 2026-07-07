 function getMax(){
    let max = 0
    for (let i = 0; i <arguments.length; i++) {
        if(arguments[i] > max){
            max = arguments[i]
        }
    }
    return max
}
