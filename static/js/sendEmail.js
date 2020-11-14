function sendMail(aboutForm) {
    emailjs.send("gmail", "template_p67sxbc", {
        "from_name": aboutForm.from_name.value,
        "reply_to": aboutForm.reply_to.value,
        "message": aboutForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // block page reload
}