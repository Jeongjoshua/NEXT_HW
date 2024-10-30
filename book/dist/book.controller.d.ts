import { BookService } from './book.service';
export declare class BookController {
    bookService: BookService;
    constructor();
    getAllPosts(): any[];
    createPost(postDto: any): string;
    getPost(id: string): any;
    deletePost(id: string): string;
    updatePost(id: string, postDto: any): {
        updatedDt: Date;
        id: string;
        title: string;
        name: string;
        createdDt: Date;
        isAvailable: boolean;
    };
}
