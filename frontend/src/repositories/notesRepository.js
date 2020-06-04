import Repository from './repository'

const resource = '/notes'
export default {
  get() {
    return Repository.get(`${resource}`);
  },
  getNote(noteId) {
    return Repository.get(`${resource}/${noteId}`);
  },
  createNote(payload) {
    return Repository.post(`${resource}`, payload);
  },
  deleteNote(noteId, password) {
    return Repository.delete(`${resource}/${noteId}?pwd=${password}`);
  },
  addNoteReply(noteId, payload) {
    return Repository.post(`${resource}/${noteId}/replies`, payload)
  }
}
