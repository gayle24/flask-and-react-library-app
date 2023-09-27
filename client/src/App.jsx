import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [salamu, setSalamu] = useState('')

  //fetch("url").then()
  useEffect(()=>{
    fetch('/api').then((r)=>r.json()).then(data=>setSalamu(data.hello));
  }, [])
  return (
    <>
      
      <h1>Library App</h1>
      <h1>{salamu}</h1>
      
    </>
  )
}

export default App
