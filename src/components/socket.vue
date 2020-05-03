<template>
    <div>
        <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">打开chat-room</el-button>
        <el-drawer title="我是标题" :visible.sync="drawer" :with-header="false">
            <div class="bottom">
                <h3 style="text-align: center">{{ title }}</h3>
                <div class="chat_box">
                    <el-scrollbar style="height: 600px" ref="scroll">
                        <ul>
                            <li v-for="mes in chat_message">{{mes.name}}: {{ mes.message }}</li>
                        </ul>
                    </el-scrollbar>
                </div>
                <div style="margin-top: 10px">
                    <el-input v-model="message" @keyup.enter.native="send"></el-input>
                </div>
                <div class="send">
                    <div></div>
                    <el-input v-model="name" style="width: 100px"></el-input>
                    <el-button @click="send" style="width: 200px" type="primary">send</el-button>
                </div>
            </div>


        </el-drawer>



    </div>
</template>

<script>
import io from 'socket.io-client';
import { baseUrl } from '@/common.js';
    export default {
        name: "socket",
        data(){
            return{
                title:'chat-room',
                socket:'',
                message:'',
                name:'你的名字',
                chat_message:[],
                drawer:false
            }
        },
        methods:{
            SocketOn(){
                // 建立一个socket连接
                this.socket = io(baseUrl+'/chat', {'reconnection':false});
                this.socket.on('my response', (res)=>{
                    // console.log(res)
                });
                this.socket.on('chat', (res)=>{
                    console.log(res);
                    this.chat_message.push(res)
                })
            },
            SocketDisconnect(){
                //断开连接
                this.socket.disconnect()
            },
            send(){
                console.log('send !');
                if(this.message != ''){
                    this.socket.emit('chat', {'name':this.name, 'message':this.message}, (data)=>{
                        this.message = '';
                        this.scrollDown()
                    })
                }

            },
             scrollDown() {
                this.$refs['scroll'].wrap.scrollTop = this.$refs['scroll'].wrap.scrollHeight
             }

        },
        created(){
            this.SocketOn()
        }
    }
</script>

<style scoped>
    .send{
        margin-top: 5px;
    }
    .chat_box >>> .el-scrollbar__wrap {
      overflow-x: hidden;
    }
    .chat_box{
        background-color: #f8f3eb;
    }
    .bottom{
        position: fixed;
        bottom: 0px;

    }
</style>