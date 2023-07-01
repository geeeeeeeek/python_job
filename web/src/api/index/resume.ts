// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
    detail = '/myapp/index/resume/detail',
    create = '/myapp/index/resume/create',
    update = '/myapp/index/resume/update',
}

const detailApi = async (params: any) => get<any>({ url: URL.detail, params: params, data: {}, headers: {} });
const createApi = async (data: any) =>
    post<any>({ url: URL.create, params: {}, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const updateApi = async (params:any, data: any) =>
    post<any>({ url: URL.update,params: params, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });

export { detailApi, createApi, updateApi };
