import Axios from 'axios'

export function get(url,params){
    return Axios.get(url,params)
}

export function post(url,params){
    return Axios.post(url,params)
}

export function del(url,params){
    return Axios.delete(url,params)
}
