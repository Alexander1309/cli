example_node_js = """const express = require('express')
const mongoose = require('mongoose')
const morgan = require('morgan')
const cors = require('cors')
require('dotenv').config()

const PORT = process.env.PORT || 3000
const CONNECTION = mongoose.connection
const app = express()

mongoose.connect(process.env.CONEXION_DB)
CONNECTION.on('error', () => console.log('Database not connect...'))
CONNECTION.once('open', () => console.log('Database conected...'))

app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(cors())
app.use(morgan('dev'))

app.listen(PORT, () => console.log(`Server run on port ${PORT}`))
"""

example_node_js_env = """PORT = 3001
CONEXION_DB =  mongodb://127.0.0.1:27017/
"""

example_node_js_pack = """"scripts": {
    "start": "node ./src",
    "dev": "nodemon ./src"
  }
"""