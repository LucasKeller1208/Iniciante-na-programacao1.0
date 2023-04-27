/*function soma( a, b) {
    return a + b;
}
console.log( soma( 1, 2 ) ); */

let tmp = "";

// function mudaCor() {
    
//     let r = 0;
//     let g = 0;
//     let b = 0;

//     //Math
//     r = Math.ceil(Math.random() * 255);
//     g = Math.ceil(Math.random() * 255);
//     b = Math.ceil(Math.random() * 255);

//     const elementos = [...document.getElementsByClassName("cabecalho")];
    
//     elementos.forEach((el)=>{
//         el.style.backgroundColor = `rgb(${r},${g},${b})`;
//     })

//     tmp = setTimeout(mudaCor, 5000);
// }

mudaBanner1()

function mudaBanner1() {
    
    let banner1 = "./img/banner-1440x300-1.jpg";
    const elImg = document.querySelector(".cabecalho > img");
    elImg.src = banner1;
    setTimeout(mudaBanner2, 2000);
}

function mudaBanner2() {
    
    let banner2 = "./img/banner-1440x300-2.jpg";
    
    const elImg = document.querySelector(".cabecalho > img");
    elImg.src = banner2;
    
    setTimeout(mudaBanner3, 2000);
}

function mudaBanner3() {
    
    let banner3 = "./img/banner-1440x300-3.jpg"

    const elImg = document.querySelector(".cabecalho > img");
    elImg.src = banner3;
    setTimeout(mudaBanner1, 2000);
}