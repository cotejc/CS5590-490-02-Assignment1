treeJSON = d3.json("package.json", function(error, treeData) {

    createTree(treeData,"#treecontainerDetalle",false);
    createTree(treeData,"#treecontainer",true);


});/**
 * Created by Jeremiah on 7/21/2017.
 */
