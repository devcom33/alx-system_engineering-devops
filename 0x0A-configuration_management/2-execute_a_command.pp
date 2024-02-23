
#Using Puppet, create a manifest that kills a process named killmenow

exec {'execute_a_command':
command => 'pkill killmenow'
}
