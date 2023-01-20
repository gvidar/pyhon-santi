const btnDelete = document.querySelectorAll('.btndelete')
if (btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click',(e)=>{ 
            if (!confirm('Estas seguro/a de eliminar el dato')){
                e.preventDefault();
            }

        });
    });


}