function blue_print(question,choice="", question_number,id){
    var choice=choice.split(";")
    return `
        <div class="accordion-item">
        <h2 class="accordion-header" id="question${question_number*2}">
            <button class="accordion-button" type="button" data-mdb-toggle="collapse"
                data-mdb-target="#collapse${question_number*2}" aria-expanded="true" aria-controls="collapse${question_number*2}">
                Question ${question_number}
            </button>
        </h2>
        <div id="collapse${question_number*2}" class="accordion-collapse collapse " aria-labelledby="headingOne"
            data-mdb-parent="#questions">
            <div class="accordion-body">
                ${question}
                <select class=" mb-2 btn btn-outline-light-grey btn-block"  data-question-id="${id}">
                <option value="select answer">Select Answer</option>
                ${choice.map((item,index)=>{
                    return `
                    <option value="${item}">${item}</option>
                    `
                }).join("")}
                </select>
                
            </div>
        </div>
    </div>
    `
}

var store={}
function get_questions(btn){
    module_name=btn.getAttribute("data-module-name")
    store["module_name"]=module_name
    console.log(module_name)

    $("#questions").html("")
    $.post("/get-questions",JSON.stringify({"module_name":module_name}),(data)=>{

        if(data==null ){
            alert("no data found")
               setTimeout(() => {
               
                $("#info_modal").modal("hide")
               }, 20);
               return false
           }
        // if thes no data for the module 
       if(data.length==0 ){
        alert("no data found")
           setTimeout(() => {
           
            $("#info_modal").modal("hide")
           }, 20);
       }
       data.map((item,index)=>{
           $("#questions").append(blue_print(item.question,item.choice,index+1,item.id))
       })
    });
}


$("#submit_questions").click(e=>{
    // get all slect values
    $(".accordion-item select").each((e, elem) => {
        key = elem.getAttribute("data-question-id").trim()
        value = $(elem).val().trim()
        store[key] = value
    });
    error=0
    Object.keys(store).map(key=>{
        var value=store[key].trim()
        if(value=="select answer"){
            error=1
        }
    })

    if(error>0){
        alert("please answer all questions")
        return false
    }


    console.log(store)

    $.post("/save-marks",JSON.stringify(store),(data)=>{
       console.log(data)
       
       if("status" in  data) window.location.reload()
       else alert("sorry we have a technical isssue at the moment")
     });

})
