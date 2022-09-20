async function sendMessage() {
    let fd = new FormData(); //fd = formdata
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')
    console.log(csrf_token)
    fd.append('textmessage', messageField.value);
    fd.append('csrfmiddlewaretoken', csrf_token[0].value);
    try {
        messages.innerHTML += `
        <div class="message" id="deleteMessage">
        <div style=" color: grey;"> {{ request.user.first_name }}: <i> ${ messageField.value } </i></div><span style="font-size: 10px; color: grey;"></span>
    </div>`;
        let response = await fetch('/chat/', {
            body: fd,
            method: 'POST',
        })
        let json = await response.json()
        console.log(json)
        console.log(json.model)
        deleteMessage.remove();
        messages.innerHTML += `
        <div class="message" id="deleteMessage">
        <div> ${ json['model']}: <i> ${ messageField.value } </i></div><span style="font-size: 10px; color: blue;">[]</span>
    </div>`;



    } catch (e) {
        console.error('An error occured!', e)
    }

    messageField.value; // let messageField = document.getElementById('messageField').value ist heutzutage nicht mehr wirklich nötig, da die brower das auch so erkennen! 

}