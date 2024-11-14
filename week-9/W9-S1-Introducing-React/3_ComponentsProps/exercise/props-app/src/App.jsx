import { useState } from 'react'
import './App.css'
import Student from './components/student'

function App() {
  const [count, setCount] = useState(0)
  const students = [
    {name: 'John', age: 20},
    {name: 'Jason', age: 30},
    {name: 'Jeev', age: 40},
    {name: 'Janice', age: 15},
    {name: 'Jasmine', age: 60},        
  ];

  return (
    <>
      <div>
        <h1>Student list</h1>
        <ul>
          {students
            .slice(0, count + 1)
            .map((student, index) => <Student key={index} name={student.name} age={student.age}/>
          )}
        </ul>
        <button onClick={
          () => {
            if (count < students?.length - 1) {
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
