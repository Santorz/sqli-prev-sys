//Selct elements

let main_control_div = document.querySelector('.main-control');
let db_type_options = Array.from(document.querySelectorAll('.db-type-option'));
let query_input_div = document.querySelector('.query-input-div');

// Setting variables
let hasInputBoxShown = false;
let all_query_arr = [];


for ( let i = 0; i < db_type_options.length; i++){

    let each_db_type_option = db_type_options[i];
    const filteredItems = db_type_options.filter((value, index) => index !== i);

    each_db_type_option.onclick = function(){
        makeDBtypeOptionSelected(each_db_type_option);
        
        for (i in filteredItems){
            if (filteredItems[i].firstElementChild.classList.contains('bold-tick'))
            removeDBtypeOptionSelected(filteredItems[i]);
        }

        let dbname = each_db_type_option.textContent.split(' ')[0].toLowerCase();

        if(!hasInputBoxShown){
            createDBQueryBox(dbname)
            for(i in filteredItems){
                makeDBtypeOptionGreyedOut(filteredItems[i])
            }
            hasInputBoxShown = true
        }

        let json_location = "../../"+dbname+'.json'

        readJSON(json_location)



    }

}


function makeDBtypeOptionSelected (element){
    element.firstElementChild.classList.add('bold-tick');
    element.classList.add('heavily-box-shadowed');
    element.classList.add('whitened');
    element.classList.add('bolded');
}
function removeDBtypeOptionSelected (element){
    element.firstElementChild.classList.remove('bold-tick');
    element.classList.remove('heavily-box-shadowed');
    element.classList.remove('whitened');
    element.classList.remove('bolded');
}

function createDBQueryBox (dbname){

    if (hasInputBoxShown == false){
        let form = document.createElement('form');
        form.method = 'post';

        let query_textbox = document.createElement('input');
        query_textbox.className = 'query-textbox';
        query_textbox.id = dbname + ' query-textbox';
        query_textbox.name = 'db-query';

        let signin_button = document.createElement('button');
        signin_button.className = 'signin';
        signin_button.textContent = 'Login'

        form.appendChild(query_textbox);
        form.appendChild(signin_button);

        query_input_div.append(form);


        // Target click on button
        signin_button.onclick = function(e){
            e.preventDefault()
            if (query_textbox.value !== ""){
                for (let i in all_query_arr){
                    let extracted_query = all_query_arr[i];
                    if (query_textbox.value == extracted_query){
                        alert('DANGER')
                        break
                    }
                    else{
                        alert('SOMEHOW SAFE')
                        break
                    }
                }
            }

        }

    }
    
}

function makeDBtypeOptionGreyedOut (element){
    element.classList.add('i-am-unclikable');
    element.classList.add('greyed-out');
    element.classList.add('z-index-reduced-by-1');
}




function readJSON (json_file) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4){

        var post = xmlhttp.responseText;
        var json_data = JSON.parse(post);

        for (let i in json_data){
            for (var key of Object.keys(json_data[i])) {
                let all_queries = json_data[i][key]
                all_query_arr.push(all_queries)
            }
        }
    
        
    }





}; //end onreadystate

xmlhttp.open("GET", json_file, true);
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

xmlhttp.send();

} // end init function