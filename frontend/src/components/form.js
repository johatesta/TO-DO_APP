import React from 'react'

function form({addTodo}) {
    const [title, setTitle] = useState('')
	const [description, setDescription] = useState('')

	const addTodoHandler = e => {
		e.preventDefault()
		addTodo({
			title,
			description,
			completed: false,
		})
	}
    return (
        <Form>
			<Form.Group controlId='title'>
			  <Form.Label>Title</Form.Label>
			  <Form.Control type='text' placeholder='Enter To-Do Title' onChange={e => setTitle(e.target.value)} />
			</Form.Group>

			<Form.Group controlId='description'>
			  <Form.Label>Description</Form.Label>
			  <Form.Control type='text' placeholder='Enter Description' onChange={e => setDescription(e.target.value)} />
			</Form.Group>

			<Button variant='primary' type='submit' onClick={addTodoHandler}>Add Todo</Button>
		</Form>
    )
}

export default form
