$("#change-submit-button").click(e=>{
    var reset = [".change-semester-error",".change-year-error"]
    reset.map(e => {
        $(e).html("")
    });

    store = {}


    // get all slect values
    $("#change_semester_modal select").each((e, elem) => {
        key = elem.getAttribute("id").split("-")[1].trim()
        value = $(elem).val()
        store[key] = value
    });

        console.log(store)
    $.post("/updateSemester", JSON.stringify(store), (response) => {
        console.log(response)
        if ("error" in response) {
            delete response["error"]
            Object.keys(response).map(key => {
                // loop in the error classes and check if the response and 
                //error class have the same name else display the error
                value = response[key]

                reset.map(elem => {
                    if (elem.includes(key)) {
                        $(elem).append(value)
                    }
                });
            });
            return false;
        }
        
        if("status" in response) window.location.reload()
        else alert("sorry we have a technical isssue at the moment")

    });
})