
function confirmDelete(id){
	let value = confirm('¿Desea eliminar el contacto?')
	if (value)
		location.href = '/delete/'+id
}
