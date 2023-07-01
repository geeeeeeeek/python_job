// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
    listUserPostUrl = '/myapp/index/post/list_user_post_api',
    listCompanyPostUrl = '/myapp/index/post/list_company_post_api',
    create = '/myapp/index/post/create',
}

const listUserPostApi = async (params: any) => get<any>({ url: URL.listUserPostUrl, params: params, data: {}, headers: {} });
const listCompanyPostApi = async (params: any) => get<any>({ url: URL.listCompanyPostUrl, params: params, data: {}, headers: {} });
const createApi = async (data: any) =>
    post<any>({ url: URL.create, params: {}, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });

export { listUserPostApi, listCompanyPostApi, createApi };
