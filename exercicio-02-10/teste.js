let titulo = document.getElementById('titulo')
titulo.textContent = "Olá!"

let botao = document.getElementById('botao')
botao.textContent = "Botão"

const frutas = ["Banana", "Maçã", "Laranja"]
const lista = document.getElementById('lista')


botao.addEventListener("click", function(){
    titulo.textContent = "Mudou geral"
    for(let i=0; i<frutas.length; i++){;
    let item = document.createElement('li');
    item.textContent = frutas[i];
    lista.appendChild(item);
    lista.classList.add("remove-ponto");
    }
});