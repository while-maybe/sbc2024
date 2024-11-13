import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const student_names = ['John', 'Jason', 'Jeev', 'Janice', 'Jasmine']

  return (
    <>

      <div>
        <h1>Student list</h1>
        <ul>
          {student_names.slice(0, count + 1 ).map((person, index) => <li key={index}>{person}</li>)}
        </ul>
        <button onClick={
          () => {
            if (count < student_names?.length - 1) {
              setCount((count) => count + 1)
            }
          }
        }>
        students: {count + 1}
        </button>
      </div>

    </>
  )
}

export default App
