$("#register-submit-button").click(e => {
    var reset = [
        ".register-program-error",
        ".register-password-error",
        ".register-email-error",
        ".register-name-error",
        ".register-course-error",
        ".register-year-error",
        ".register-semester-error",
    ]
    reset.map(e => {
        $(e).html("")
    });

    // get  all input  values
    store = {}
    $("#registerModal input").each((e, elem) => {
        key = elem.getAttribute("id").split("-")[1].trim()
        value = $(elem).val()
        store[key] = value
    });

    // get all slect values
    $("#registerModal select").each((e, elem) => {
        key = elem.getAttribute("id").split("-")[1].trim()
        value = $(elem).val()
        store[key] = value
    });

    $.post("/register", JSON.stringify(store), (response) => {
        // get the datat
        console.log(response)
        if ("error" in response) {
            delete response["error"]
            Object.keys(response).map(key => {
                // loop in the error classes and check if the response and 
                //error class have the same name else display the error
                value = response[key]

                reset.map(elem => {
                    if (elem.includes(key)) {
                        $(elem).html(value)
                    }
                });
            });
            return false;
        }
        
        if("status" in response) window.location.reload()
        else alert("sorry we have a technical isssue at the moment")
    });
})