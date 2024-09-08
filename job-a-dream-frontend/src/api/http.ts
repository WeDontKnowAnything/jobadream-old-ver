import axios from 'axios'

// const BaseURL: string = 'api.jobadream.com'
// const Port = 443
const BaseURL: string = location.host.split(':')[0]
const Port = 8000

// const http = axios.create({ baseURL: `https://${BaseURL}:${Port}` })
const http = axios.create({ baseURL: `http://${BaseURL}:${Port}` })
export { http }
