"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BookService = void 0;
class BookService {
    constructor() {
        this.posts = [];
    }
    getAllPosts() {
        return this.posts;
    }
    createPost(postDto) {
        const id = this.posts.length + 1;
        this.posts.push({ id: id.toString(), ...postDto, createdDt: new Date() });
    }
    getPost(id) {
        const post = this.posts.find((post) => {
            return post.id === id;
        });
        console.log(post);
        return post;
    }
    delete(id) {
        const filteredPosts = this.posts.filter((post) => post.id !== id);
        this.posts = [...filteredPosts];
    }
    updatePost(id, PostDto) {
        let updateIndex = this.posts.findIndex((post) => post.id === id);
        const updatePost = { id, ...PostDto, updatedDt: new Date() };
        this.posts[updateIndex] = updatePost;
        return updatePost;
    }
}
exports.BookService = BookService;
//# sourceMappingURL=book.service.js.map