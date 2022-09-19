    const elem = document.getElementById('actions_list_add');
    const btn = document.getElementById('add_btn');
    elem.remove()

    btn.addEventListener('click', function(){
        if (document.contains(elem)) {
            elem.remove();
    }   else {
        document.body.appendChild(elem);
    }   
    });
    
    
