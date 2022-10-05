async function sendMessage() {
    let fd = new FormData(); //fd = formdata
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')
    fd.append('textmessage', messageField.value);
    fd.append('csrfmiddlewaretoken', csrf_token[0].value);
    try {
        messages.innerHTML += `
        <div class="message" id="deleteMessage">
        <div style=" color: grey;"> You : <i> ${ messageField.value } </i></div><span style="font-size: 10px; color: grey;"></span>
    </div>`;
        let response = await fetch('/chat/', {
            body: fd,
            method: 'POST',
        })
        let json = await response.json()
        console.log(json) //nur zum zum arbeiten atm kommt dann weg
        console.log(JSON.parse(json['data'][0])) //nur zum zum arbeiten atm kommt dann weg
        let userData = JSON.parse(json['data'][0])
        deleteMessage.remove();
        messages.innerHTML += `
        <div class="message">
        <div> ${ json['data'][1]['user']}: <i> ${ messageField.value } </i></div><span style="font-size: 10px; color: blue;">[${ userData['fields']['created_at']}]</span>
    </div>`;



    } catch (e) {
        console.error('An error occured!', e)
    }

    messageField.value; // let messageField = document.getElementById('messageField').value ist heutzutage nicht mehr wirklich nötig, da die brower das auch so erkennen! 

}