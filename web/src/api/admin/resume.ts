// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
    list = '/myapp/admin/resume/list',
    create = '/myapp/admin/resume/create',
    update = '/myapp/admin/resume/update',
    delete = '/myapp/admin/resume/delete',
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });
const createApi = async (data: any) =>
    post<any>({ url: URL.create, params: {}, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const updateApi = async (params:any, data: any) =>
    post<any>({ url: URL.update,params: params, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const deleteApi = async (params: any) => post<any>({ url: URL.delete, params: params, headers: {} });

export { listApi, createApi, updateApi, deleteApi };
