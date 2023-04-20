//фунционал с модалкой


const buttonAdd = document.querySelector('.noticeboard__add')
const wrapper = document.querySelector('.wrapper')
const modalWindow = document.createElement("div")
modalWindow.className = "modalWindow"
const modalWindowContent = document.createElement("div")
modalWindowContent.className = "modalWindowContent"
const modalWindowContentTitle = document.createElement("div")
modalWindowContentTitle.className = "modalWindow__title"
modalWindowContentTitle.innerText = "НОВОЕ ОБЪЯВЛЕНИЕ"
const modalWindowContentForm = document.createElement("form")
modalWindowContentForm.className = "modalWindow__form"
const modalWindowContentFormInputTitle = document.createElement("input")
modalWindowContentFormInputTitle.className = "modalWindow__form-inputTitle"
modalWindowContentFormInputTitle.type = "text"
modalWindowContentFormInputTitle.placeholder = "название объявления"
const modalWindowContentFormInputText = document.createElement("textarea")
modalWindowContentFormInputText.className = "modalWindow__form-inputText"
modalWindowContentFormInputText.type = "text"
modalWindowContentFormInputText.placeholder = "описание объявления"
const modalWindowContentButton = document.createElement("button")
modalWindowContentButton.className = "modalWindow__button"
modalWindowContentButton.innerText = "ДОБАВИТЬ"
const closeButton = document.createElement("i")
closeButton.className = "uil uil-times"


buttonAdd.onclick = () => {
    if (!wrapper.querySelector('.modalWindow')) {
        wrapper.style.height = "100%"
        wrapper.appendChild(modalWindow)
        modalWindow.appendChild(modalWindowContent)
        modalWindowContent.appendChild(closeButton)
        modalWindowContent.appendChild(modalWindowContentTitle)
        modalWindowContent.appendChild(modalWindowContentForm)
        modalWindowContentForm.appendChild(modalWindowContentFormInputTitle)
        modalWindowContentForm.appendChild(modalWindowContentFormInputText)
        modalWindowContentForm.appendChild(modalWindowContentButton)
        closeButton.onclick = () => {
            wrapper.removeChild(modalWindow)
            wrapper.style.height = ""
            modalWindowContent.remove()
            closeButton.remove()
            modalWindowContentTitle.remove()
            modalWindowContentFormInputTitle.remove()
            modalWindowContentFormInputText.remove()
            modalWindowContentButton.remove()
        }
        modalWindowContentButton.onclick = () => {
            wrapper.removeChild(modalWindow)
            wrapper.style.height = ""
            const noticeboard = document.querySelector(".noticeboard")
            const infoblockList = document.querySelectorAll(".noticeboard__infoblock")
            const newInfoBlock = document.createElement("div")
            newInfoBlock.className = "noticeboard__infoblock";
            const newInfoBlockID = infoblockList.length + 1;
            newInfoBlock.id = `block${newInfoBlockID}`
            noticeboard.appendChild(newInfoBlock)
            const newInfoBlockHead = document.createElement("div")
            newInfoBlockHead.className = "noticeboard__infoblock-header"
            newInfoBlock.appendChild(newInfoBlockHead)
            const newInfoBlockTitle = document.createElement("div")
            const newInfoBlockDate = document.createElement("div")
            newInfoBlockTitle.className = "noticeboard__infoblock-title"
            newInfoBlockTitle.innerText = modalWindowContentFormInputTitle.value;
            let date = new Date();
            newInfoBlockDate.className = "noticeboard__infoblock-date"
            newInfoBlockDate.innerText = " " + date.getDate() + ".0" + (date.getMonth() + 1) + "." + date.getFullYear() + " " + date.getHours() + ":" + ((date.getMinutes() < 10 ? '0' : '') + date.getMinutes())
            newInfoBlockHead.appendChild(newInfoBlockTitle)
            newInfoBlockHead.appendChild(newInfoBlockDate)
            const newInfoBlockText = document.createElement("div")
            newInfoBlockText.className = "noticeboard__infoblock-text"
            newInfoBlockText.innerText = modalWindowContentFormInputText.value
            newInfoBlock.appendChild(newInfoBlockText)
            const newInfoBlockButtons = document.querySelector(".noticeboard__infoblock-buttons").cloneNode(true);

            newInfoBlock.appendChild(newInfoBlockButtons);

            const buttonEdit = newInfoBlockButtons.children[0];
            const buttonDelete = newInfoBlockButtons.children[1];

            modalWindowContentFormInputTitle.value = ""
            modalWindowContentFormInputText.value = ""

            buttonEdit.addEventListener('click', editBlock)
            buttonDelete.addEventListener('click', deleteBlock)
            modalWindowContentTitle.remove()
            modalWindowContentButton.remove()
        }
    }
}



//фунционал кнопки "удалить"


let buttonsDelete = document.querySelectorAll('.delete')

buttonsDelete.forEach((buttonDelete) => {
    buttonDelete.addEventListener('click', deleteBlock)
})
function deleteBlock(ev){
    let parentBlock = ev.target.parentNode.parentNode
    parentBlock.remove()
}


//функционал кнопки "изменить"

let buttonsEdit = document.querySelectorAll('.edit')

buttonsEdit.forEach((buttonEdit) => {
    buttonEdit.addEventListener('click', editBlock)
})

function editBlock(ev) {
    let parentBlock = ev.target.parentNode.parentNode;
    wrapper.style.height = "100%"
    modalWindowContentFormInputTitle.value = parentBlock.children[0].children[0].innerText
    modalWindowContentFormInputText.value = parentBlock.children[1].innerText
    wrapper.appendChild(modalWindow)
    modalWindow.appendChild(modalWindowContent)
    modalWindowContent.appendChild(closeButton)
    const modalWindowContentTitle = document.createElement('div');
    modalWindowContentTitle.className = "modalWindow__title";
    modalWindowContentTitle.innerText = "ИЗМЕНИТЬ ОБЪЯВЛЕНИЕ"
    modalWindowContent.appendChild(modalWindowContentTitle)
    modalWindowContent.appendChild(modalWindowContentForm)
    modalWindowContentForm.appendChild(modalWindowContentFormInputTitle)
    modalWindowContentForm.appendChild(modalWindowContentFormInputText)
    const modalWindowContentEditButton = document.createElement("div");
    modalWindowContentEditButton.className = "modalWindow__button"
    modalWindowContentEditButton.innerText = "ИЗМЕНИТЬ"
    modalWindowContentForm.appendChild(modalWindowContentEditButton)
    closeButton.onclick = () => {
        wrapper.removeChild(modalWindow)
        wrapper.style.height = ""
        modalWindowContent.remove()
        closeButton.remove()
        modalWindowContentTitle.remove()
        modalWindowContentForm.remove()
        modalWindowContentFormInputTitle.remove()
        modalWindowContentFormInputText.remove()
        modalWindowContentFormInputText.remove()
        modalWindowContentEditButton.remove()
        modalWindowContentFormInputTitle.value = ""
        modalWindowContentFormInputText.value = ""

    }
    modalWindowContentEditButton.onclick = () => {
        parentBlock.children[0].children[0].innerText = modalWindowContentFormInputTitle.value
        parentBlock.children[1].innerText = modalWindowContentFormInputText.value
        let date = new Date();
        parentBlock.children[0].children[1].innerText = " " + date.getDate() + ".0" + (date.getMonth() + 1) + "." + date.getFullYear() + " " + date.getHours() + ":" + ((date.getMinutes() < 10 ? '0' : '') + date.getMinutes())
        modalWindowContentFormInputTitle.value
        wrapper.removeChild(modalWindow)
        wrapper.style.height = ""
        modalWindowContent.remove()
        closeButton.remove()
        modalWindowContentTitle.remove()
        modalWindowContentForm.remove()
        modalWindowContentFormInputTitle.remove()
        modalWindowContentFormInputText.remove()
        modalWindowContentFormInputText.remove()
        modalWindowContentEditButton.remove()
        modalWindowContentFormInputText.value = ""
        modalWindowContentFormInputTitle.value = ""
    }
}




