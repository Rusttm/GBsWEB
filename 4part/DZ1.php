<?php
        // формируем массив c опытом работы
        $job = [
            'job_name' => ['GB', 'GBUniversity', 'GBSchool'],
            'job_data' => ['2022-настоящее время', '2018-2022', '2010-2018'],
            'job_desc' => ['Работа-учеба', 'Учеба-работа', 'Только практика']
] ?>

<div class="w3-container w3-card w3-white w3-margin-bottom">
    <h2 class="w3-text-grey w3-padding-16">
      <iclass="fa fa-suitcase fa-fw w3-margin-right w3-xxlarge w3-text-teal"></i>Опыт работы</h2>

<?php  
  for ($x = 0; $x <= 2; $x+=1) {
    echo '<div class="w3-container"> <h5 class="w3-opacity"><b>';
    echo $job['job_name'][$x] ;
    echo '</b></h5><h6 class="w3-text-teal"><i class="fa fa-calendar fa-fw w3-margin-right"></i>';
    echo $job['job_data'][$x] ;
    echo '</h6><p>';
    echo $job['job_desc'][$x] ;
    echo '</p><hr> </div>';
  }
?>  

</div>