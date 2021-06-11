
> 安装

    npm install -g @vue/cli

> 创建项目

    vue create {项目名}


> vue2.x -> vue3.x

    # 生命周期转变
    beforeCreate -> use setup()
    created -> use setup()
    beforeMount -> onBeforeMount
    mounted -> onMounted
    beforeUpdate -> onBeforeUpdate
    updated -> onUpdated
    beforeDestroy -> onBeforeUnmount
    destroyed -> onUnmounted
    errorCaptured -> onErrorCaptured
    

[返回目录](../README.md)