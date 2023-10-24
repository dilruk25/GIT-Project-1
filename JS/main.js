console.log("Hi ICET.....");

//var, let, const

var name = "Yasindu";

console.log(name + " Is My Name");

//function - method
function print() {
    console.log("print called..!");
}

//fuction calling statement
print();

function getData() {
    var email = document.getElementById('email').value
    console.log(email);
}



function getData1() {
    var a = parseInt(document.getElementById('a').value);
    console.log(a);

    var b = parseInt(document.getElementById('b').value);
    console.log(b);

    var c = parseInt(document.getElementById('c').value);
    console.log(c);

    var d = parseInt(document.getElementById('d').value);
    console.log(d);

    var e = parseInt(document.getElementById('e').value);
    console.log(e);


    var avg = a + b + c + d + e;
    print ("Average= +avg")

    var num=90;
    num+=2
    console.log(num);
    var num2=45;
    num2++;
    ///////////////
    function {var sub1 =89;
    var sub2 =45;
    var sub3 =90;
    var total=sub1+sub2+sub3;
    console.log("Total: "=total);
    var avg=(total)/3;
    console.log("Average marks:" +avg);
    }
