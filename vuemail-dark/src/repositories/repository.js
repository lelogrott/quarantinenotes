import axios from 'axios'

const baseDomain = 'https://ct8jn93qvb.execute-api.us-east-1.amazonaws.com'
const baseURL = `${baseDomain}/dev`

export default axios.create({
  baseURL
})
