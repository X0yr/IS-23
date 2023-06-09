function btnClick(){
    let Tex1 = ""
    let Tex2 = ""
    Tex1 = KT_3_1.Test.tx1
    Tex2 = KT_3_1.Test.tx2
    KT_3_1.getElementById('ex1').innerHTML="<HR>"+
    "Мне нравиться "+Tex1.bold() +
    "с "+ Tex2.bold() + "цветом"+"<HR>"
}