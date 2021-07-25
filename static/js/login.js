$("#login-submit-button").click(e => {
    // list of class errors
    var reset = [".login-program-error", ".login-password-error", ".login-email-error", "login-program-error"]
    // reset the values 
    reset.map(e => {
        $(e).html("")
    });

    // store the form data
    store = {}
    $("#loginModal input").each((e, elem) => {
        key = elem.getAttribute("id").split("-")[1].trim()
        value = $(elem).val()
        store[key] = value
    });

    
    $.post("/login", JSON.stringify(store), (response) => {
        // get the datat
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
});
