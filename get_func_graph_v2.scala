@main def exec(filename: String) = {
   importCode.c(filename)
   run.ossdataflow
   var func_name = cpg.method.filter(node => node.astParentType == "TYPE_DECL" && node.name != "<global>" && node.isExternal == false).name.l.head
   cpg.method(func_name).dotCfg.l |> filename + ".Cfg.dot"
   delete
}

