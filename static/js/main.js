async function sendMessage() {
    let fd = new FormData(); //fd = formdata, erstellt neues formular anstatt HTML <form>
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')
    let chId = channelId.value
    fd.append('textmessage', messageField.value);
    fd.append('csrfmiddlewaretoken', csrf_token[0].value);
    try {
        templateBeforLoaded();
        let response = await fetch(`/chat/${chId}/`, {
            body: fd,
            method: 'POST',
        })
        let json = await response.json()
        console.log(json) //nur zum zum arbeiten atm kommt dann weg
        console.log(JSON.parse(json['data'][0])) //nur zum zum arbeiten atm kommt dann weg
        let userData = JSON.parse(json['data'][0])
        let newDate = createTimeStemp(userData['fields']['created_at'])
        deleteMessage.remove();
        templateAfterLoaded(newDate, json);
        messageField.value = '';
    } catch (e) {
        console.error('An error occured!', e)
    }
}



//Utility functions


function templateBeforLoaded() {
    messages.innerHTML += `
        <div class="message" id="deleteMessage">
        <div style=" color: grey;"> You : <i> ${ messageField.value } </i></div><span style="font-size: 10px; color: grey;"></span>
        </div>`;
}


function templateAfterLoaded(newDate, json) {
    messages.innerHTML += `
        <div class="message">
        <div> ${ json['data'][1]['user'] }: <i> ${ messageField.value } </i></div><span style="font-size: 10px; color: blue;">[${ newDate }]</span>
        </div>`;
}


function createTimeStemp(date) {
    let newDate = new Date(date);
    let day = newDate.getDate();
    let year = newDate.getFullYear();
    let month = newDate.toLocaleString('en-US', { month: 'short' });
    return `${ month }, ` + `${ day }, ` + `${ year }`
}