
function remove(id){
	let value = confirm('Are you sure you want to delete it?')
	if (value){
		location.href = '/delete/'+id
	}
}
