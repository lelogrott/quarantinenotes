import axios from 'axios'

const baseDomain = 'https://kej2ab8p44.execute-api.us-east-1.amazonaws.com'
const baseURL = `${baseDomain}/dev`

export default axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json'
  }
})
