import { http } from '@/api/http'

export function getPostList() {
  return http.get('/api/v1/boards')
}

export function getPost() {
  return http.get('/api/v1/posts')
}

export function addPost(data: any) {
  return http.post('/api/v1/posts', data)
}

export function addComment(data: any) {
  return http.post('/api/v1/post/comments', data)
}
