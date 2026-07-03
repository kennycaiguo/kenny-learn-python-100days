## 1.这个项目是根据武老师的day16-20项目为蓝图创建的。这个项目其实是一个比较好的实习项目，但是它也有一个缺点，就是只有一个默认的app和一个dayxxApp，把所有的路由都放在dayxxApp里面，这个其实不太好，我们需要根据路由来创建app，查看他的路由文件，发现有dep，user,pretty,admin,task,order,chart,upload,city等等路由，还有几个如login,logout,image/code等等路由

## 2.我们的应用程序只有一个day47app应用程序，但是里面我们用一个views文件夹来代替views文件，因为如果把所有路由都放在一个文件里面，随着业务的复杂度增加，这个文件会变得非常大，很难阅读和维护，我们需要给对应的一组路由创建一个py视图文件，比如所有于dep相关的路由入dep/list/,dep/xx都在dep_view.py处理。如此类推...

