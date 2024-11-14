import { useState } from 'react'
import './App.css'
import Student from './components/Student'


function App() {
  const [count, setCount] = useState(0);
  const [selectedStudent, setSelectedStudent] = useState();
  const students = [
    {name: 'Jasmine', age: 20},
    {name: 'Jason', age: 30},
    {name: 'Jeev', age: 40},
    {name: 'Janice', age: 15},
    {name: 'John', age: 60},        
  ];

  const onClickStudent = (studentName) => {
    setSelectedStudent(studentName);
  }

  return (
    <>
      <div>
        <h1>Student list</h1>
        {selectedStudent && <h2>✋ {selectedStudent}</h2>}
        <ul>
          {students
            .slice(0, count + 1)
            .map((student, index) => <Student key={index} name={student.name} age={student.age} onClickStudent={onClickStudent}/>
          )}
        </ul>
        <button onClick={
          () => {
            if (count < students.length - 1) {
              setCount(count + 1)
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
