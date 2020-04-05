import Repository from './repository'

const resource = '/notes'
export default {
  get() {
    return Repository.get();
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
    return Repository.put(`${resource}/${noteId}`, { reply: payload })
  }
}
