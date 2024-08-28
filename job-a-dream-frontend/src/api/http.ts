import axios from 'axios'

const BaseURL: string = 'api.jobadream.com'
const Port = 443

const http = axios.create({ baseURL: `https://${BaseURL}:${Port}` })
export { http }
