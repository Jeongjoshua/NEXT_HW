import { PostDto } from './book.model';
export declare class BookService {
    posts: any[];
    getAllPosts(): any[];
    createPost(postDto: PostDto): void;
    getPost(id: any): any;
    delete(id: any): void;
    updatePost(id: any, PostDto: PostDto): {
        updatedDt: Date;
        id: string;
        title: string;
        name: string;
        createdDt: Date;
        isAvailable: boolean;
    };
}
