(this.webpackJsonpfennekwebui=this.webpackJsonpfennekwebui||[]).push([[0],{57:function(e,t,a){},58:function(e,t,a){},70:function(e,t,a){},88:function(e,t,a){},89:function(e,t,a){},90:function(e,t,a){},91:function(e,t,a){},92:function(e,t,a){},93:function(e,t,a){},95:function(e,t,a){"use strict";a.r(t);var n=a(0),o=a.n(n),s=a(31),i=a.n(s),l=(a(70),a(1)),r=a(2),c=a(8),u=a(3),d=a(4),m=a(10),h=(a(57),a(23)),p=a(64),f=a(22),g=a(24),v=(a(71),a(65)),_=(a(28),a(51)),y=a.n(_),E=(a(86),function(e){Object(u.a)(a,e);var t=Object(d.a)(a);function a(e,n){var o;return Object(l.a)(this,a),(o=t.call(this,e,n)).handleChangeComplete=function(e){o.props.handleChangeComplete(e,o.props.effect)},o.handleOnChange=function(e){o.props.handleOnChange(e,o.props.effect)},o.state={value:e.value,sound:null,effect:""},o}return Object(r.a)(a,[{key:"render",value:function(){return this.state.sound=this.props.sound,this.state.effect=this.props.effect,o.a.createElement("div",{className:"slider-vertical"},o.a.createElement(y.a,{value:this.props.value,orientation:"vertical",onChange:this.handleOnChange,onChangeComplete:this.handleChangeComplete}))}}]),a}(n.Component)),b=a(20),S=a(61),k=a(43),w=(a(88),function(e){var t=e.notesAreaWidthInPixels,a=e.timePerSequence,s=e.totalLapsedTime,i=Object(n.useRef)(null);return Object(n.useLayoutEffect)((function(){var e=Math.min(s%a/a,1);i.current.style.transform="translate3d("+(e*t).toFixed(2)+"px, 0, 0px)"}),[t,a,s]),o.a.createElement("div",{className:"play_head",ref:i})}),C=Object(n.memo)(w),O=a(16),j=a(13),N=[{id:0,title:"4-on-the-Floor",noteCount:16,trackList:[{title:"Your Sound",soundFile:"whatever",onNotes:[0,2,4,6,8,10,12,14]}]}],T=Object(n.createContext)({sequence:{},toggleNote:function(){},selectSequence:function(){}}),x=function(e,t){switch(t.type){case"SET_SEQUENCE":return Object(m.a)({},N.find((function(e){return e.id===t.value})));case"SET_ON_NOTES":var a=e.trackList.map((function(e,a){return t.trackID===a?Object(m.a)(Object(m.a)({},e),{},{onNotes:t.value}):e}));return Object(m.a)(Object(m.a)({},e),{},{trackList:a});default:return e}},P=function(e){var t=e.children,a=Object(n.useReducer)(x,Object(m.a)({},N[0])),s=Object(j.a)(a,2),i=s[0],l=s[1];return o.a.createElement(T.Provider,{value:{sequence:i,toggleNote:function(e){var t,a=e.trackID,n=e.stepID,o=i.trackList[a].onNotes;t=-1===o.indexOf(n)?[].concat(Object(O.a)(o),[n]):o.filter((function(e){return e!==n})),l({type:"SET_ON_NOTES",value:t,trackID:a})},selectSequence:function(e){l({type:"SET_SEQUENCE",value:e})}}},t)},I=a(9),A=a.n(I),D=a(15),R=function(){function e(t){Object(l.a)(this,e),this.base64ToArrayBuffer=function(e){for(var t=window.atob(e),a=t.length,n=new Uint8Array(a),o=0;o<a;o++)n[o]=t.charCodeAt(o);return n.buffer};var a=!!navigator.userAgent.match(/safari/i)&&!navigator.userAgent.match(/chrome/i)&&"undefined"!==typeof document.body.style.webkitFilter,n=window.AudioContext||window.webkitAudioContext||window.MozAudioContext;this.audioContext=new n,a&&(this.isSafariFixed=!1,this.boundSafariFix=this.safariFix.bind(this),window.addEventListener("click",this.boundSafariFix,!1)),this.buffer||this.loadSound(t)}return Object(r.a)(e,[{key:"safariFix",value:function(){if(this.isSafariFixed)window.removeEventListener("click",this.boundSafariFix,!1);else{var e=this.audioContext.createBuffer(1,1,22050),t=this.audioContext.createBufferSource();t.buffer=e,t.connect(this.audioContext.destination),t.start(0),this.isSafariFixed=!0}}},{key:"loadSound",value:function(){var e=Object(D.a)(A.a.mark((function e(t){var a;return A.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return this.recorderNode=this.audioContext.createGain(),this.recorderNode.gain.value=1,this.buffer=null,this.path=t,a=this.base64ToArrayBuffer(t),console.log(typeof a),e.next=8,this.decodeAudioDataAsync(this.audioContext,a);case 8:this.buffer=e.sent;case 9:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"decodeAudioDataAsync",value:function(e,t){return new Promise((function(a,n){e.decodeAudioData(t,(function(e){return a(e)}),(function(e){return n(e)}))}))}},{key:"play",value:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:1,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:1;this.audioContext.resume();var a=this.audioContext.createGain(),n=this.audioContext.createBufferSource();a.gain.value=e,n.playbackRate.value=t,n.buffer=this.buffer,n.connect(a),a.connect(this.recorderNode),a.connect(this.audioContext.destination),n.start(0)}}]),e}(),M=function(e){var t=Object(n.useState)({play:function(){}}),a=Object(j.a)(t,2),o=a[0],s=a[1],i=Object(n.useCallback)((function(){return o.play()}),[o]);return Object(n.useEffect)((function(){s(new R(e))}),[e]),[i]},B=a(18),L=a.n(B),F=(a(89),function(e){var t=e.trackID,a=e.stepID,s=e.isNoteOn,i=e.isNoteOnCurrentStep,l=e.play,r=Object(n.useContext)(T).toggleNote,c=L()("note",{on:s,playing:s&&i});Object(n.useEffect)((function(){s&&i&&l()}),[s,i,l]);return o.a.createElement("div",{className:c,onClick:function(e){e.target.classList.toggle("on"),r({trackID:t,stepID:a}),l()}})}),z=Object(n.memo)(F),q=(a(58),function(e){var t=e.trackID,a=e.currentStepID,n=e.title,s=e.noteCount,i=e.onNotes,l=e.soundFilePath,r=M(l),c=Object(j.a)(r,1)[0],u=Object(O.a)(Array(s)).map((function(e,n){var s=-1!==i.indexOf(n),l=a===n,r=n;return o.a.createElement(z,{key:n,trackID:t,stepID:r,isNoteOn:s,isNoteOnCurrentStep:l,play:c})}));return o.a.createElement("div",{className:"track"},o.a.createElement("header",{className:"track_title"},n),o.a.createElement("main",{className:"track_notes"},u))}),U=Object(n.memo)(q),H=function(e){var t=e.currentStepID,a=e.base64Sound,s=Object(n.useContext)(T).sequence,i=s.trackList,l=s.noteCount,r=i.map((function(e,n){var s=e.title,i=e.onNotes;e.soundFile;return o.a.createElement(U,{key:s,trackID:+n,currentStepID:t,title:s,noteCount:l,onNotes:i,soundFilePath:a})}));return o.a.createElement("div",{className:"track-list"},r)},G=Object(n.memo)(H),V=(a(90),function(e){var t=e.setStartTime,a=e.setPastLapse,s=e.setBPM,i=e.isSequencePlaying,l=e.startTime,r=e.BPM,c=Object(n.useContext)(T),u=c.sequence.id,d=c.selectSequence;return o.a.createElement("nav",{className:"toolbar"},o.a.createElement("button",{className:"form_element button_stop",onClick:function(){a(0),t(null)},"aria-label":"Stop"},o.a.createElement("svg",{width:"14",height:"14",viewBox:"0 0 14 14"},o.a.createElement("rect",{className:"button_icon_path",x:"2",y:"2",width:"10",height:"10"}))),o.a.createElement("button",{className:"form_element button_play_pause",onClick:function(){i?(a((function(e){return e+performance.now()-l})),t(null)):t(performance.now())},"aria-label":"Play / Pause"},o.a.createElement("svg",{width:"14",height:"14",viewBox:"8 8 20 20"},i&&o.a.createElement("path",{className:"button_icon_path",id:"pause-icon","data-state":"playing",d:"M11,10 L17,10 17,26 11,26 M20,10 L26,10 26,26 20,26"}),!i&&o.a.createElement("path",{className:"button_icon_path",id:"play-icon","data-state":"paused",d:"M11,10 L18,13.74 18,22.28 11,26 M18,13.74 L26,18 26,18 18,22.28"}))),o.a.createElement("input",{className:"form_element input_bpm",id:"bpm",type:"text",value:r,onChange:function(e){s(e.target.value)}}),o.a.createElement("label",{className:"label_bpm",htmlFor:"bpm"},"BPM"),o.a.createElement("select",{className:"form_element select_sequence",value:u,onChange:function(e){return d(+e.target.value)},"aria-label":"Select sequence"},N.map((function(e){return o.a.createElement("option",{key:e.id,value:e.id},e.title)}))))}),J=Object(n.memo)(V),K=(a(91),function(e){var t=e.count,a=void 0===t?0:t,n=Object(O.a)(Array(a)).map((function(e,t){return o.a.createElement("div",{className:"step",key:t+1},t+1)}));return o.a.createElement("div",{className:"steps"},n)}),W={__app_visibility:"visible",__color_bg:"#505050",__color_fg:"#f5f5f5",__color_black:"#000",__color_dark_grey:"#2e2e2e",__color_light_grey:"#5d5d5d",__color_highlight:"#37e147",__base_font_size:12,__number_of_steps:16,__number_of_tracks:4,__grid_unit:2,__play_head_width:2,__form_element_height:30,__input_bpm_width:45,__step_height:32,__track_title_width:120,__note_width:32,__note_height:49,__note_border_size:1,__note_margin_vert:5,__note_margin_horz:4},Y=W.__note_width+2*W.__note_margin_horz,Q=W.__note_height+2*W.__note_margin_vert,$=function(e){return Y*e-W.__play_head_width/2},X=function(e,t){return document.documentElement.style.setProperty(e,t)},Z=function(e){return Object(n.useEffect)((function(){!function(e){W.__number_of_steps=e,X("--app-visibility",W.__app_visibility),X("--color-bg",W.__color_bg),X("--color-fg",W.__color_fg),X("--color-black",W.__color_black),X("--color-dark-grey",W.__color_dark_grey),X("--color-light-grey",W.__color_light_grey),X("--color-highlight",W.__color_highlight),X("--base-font-size",W.__base_font_size+"px"),X("--number-of-steps",W.__number_of_steps),X("--play-head-width",W.__play_head_width+"px"),X("--play-head-height",Q*W.__number_of_tracks-2*W.__note_margin_vert+"px"),X("--spacer",5*W.__grid_unit+"px"),X("--form-element-height",W.__form_element_height+"px"),X("--button-pause-play-width",W.__form_element_height+"px"),X("--input-bpm-width",W.__input_bpm_width+"px"),X("--step-height",W.__step_height+"px"),X("--track-title-width",W.__track_title_width+"px"),X("--note-border-size",W.__note_border_size+"px"),X("--note-width",W.__note_width+"px"),X("--note-height",W.__note_height+"px"),X("--note-margin-vert",W.__note_margin_vert+"px"),X("--note-margin-horz",W.__note_margin_horz+"px"),X("--note-width-full",Y+"px"),X("--left-gutter-size",W.__track_title_width+5*W.__grid_unit*2+"px"),X("--all-note-widths",Y*W.__number_of_steps+"px"),X("--app-max-width",W.__track_title_width+5*W.__grid_unit*2+(W.__note_width+2*W.__note_margin_horz)*W.__number_of_steps+"px")}(e)}),[e]),[$]},ee=function(e){var t=Object(n.useState)(null),a=Object(j.a)(t,2),o=a[0],s=a[1];return Object(n.useLayoutEffect)((function(){if(e){var t=requestAnimationFrame((function(){return s(performance.now())}));return function(){return cancelAnimationFrame(t)}}}),[e,o]),e?o:null};a(92);var te=function(e){var t=e.base64Sound,a=e.startTime,s=e.pastLapsedTime,i=e.BPM,l=e.setStartTime,r=e.setPastLapse,c=e.setBPM,u=16,d=Object(n.useState)(null),m=Object(j.a)(d,2),h=m[0],p=m[1],f=Z(u),g=(0,Object(j.a)(f,1)[0])(u),v=60/i*1e3*8,_=v/u,y=null!==a,E=ee(y),b=s+(y?Math.max(0,E-a):0);Object(n.useEffect)((function(){p(y?Math.floor(b/_)%u:null)}),[y,_,b,u]);var S={setStartTime:l,setPastLapse:r,setBPM:c,isSequencePlaying:y,startTime:a,BPM:i},k={notesAreaWidthInPixels:g,timePerSequence:v,totalLapsedTime:b},w={currentStepID:h};return o.a.createElement(P,null,o.a.createElement("main",{className:"app"},o.a.createElement("header",{className:"app_header"},o.a.createElement("h1",{className:"app_title"}),o.a.createElement(J,S)),o.a.createElement(K,{count:u}),o.a.createElement("div",{className:"app_content"},o.a.createElement(C,k),o.a.createElement(G,{base64Sound:t,currentStepID:w.currentStepID}))))},ae=function(e){var t=new Date(parseInt(e));return t.getDate()+"."+(t.getMonth()+1)+"."+t.getFullYear()+" "+t.getHours()+":"+t.getMinutes()},ne=a(52),oe=a(54),se=a(33),ie=(a(93),function(e){Object(u.a)(a,e);var t=Object(d.a)(a);function a(){return Object(l.a)(this,a),t.apply(this,arguments)}return Object(r.a)(a,[{key:"render",value:function(){return this.props.visualizations&&0!==this.props.visualizations.length?o.a.createElement(se.a,{style:{"text-align":"center"}},o.a.createElement(se.a.Toggle,{as:g.a,variant:"link",eventKey:"0"},"Show Visualizer"),o.a.createElement(se.a.Collapse,{eventKey:"0"},o.a.createElement(oe.a,null,this.props.visualizations.map((function(e){return o.a.createElement(oe.a.Item,null,o.a.createElement("h3",null,e.name),o.a.createElement(ne.a,{style:{width:"80%",height:"auto"},src:"data:image/png;base64,"+e.base64img,rounded:!0}))}))))):null}}]),a}(o.a.Component)),le=a(62),re=a.p+"static/media/1600px-Logo_KIT.6ba029f8.png",ce=a.p+"static/media/refresh_icon.d18b1ef2.svg";a(27);var ue=a(63),de=a.n(ue),me={flex:1,display:"flex",flexDirection:"column",alignItems:"center",padding:"20px",borderWidth:2,borderRadius:2,borderColor:"#eeeeee",borderStyle:"dashed",backgroundColor:"#fafafa",color:"#bdbdbd",outline:"none",transition:"border .24s ease-in-out"},he={borderColor:"#2196f3"},pe={borderColor:"#00e676"},fe={borderColor:"#ff1744"};function ge(e){var t=Object(v.a)({accept:"audio/wav",onDrop:e.onDrop}),a=t.getRootProps,s=t.getInputProps,i=t.isDragActive,l=t.isDragAccept,r=t.isDragReject,c=Object(n.useMemo)((function(){return Object(m.a)(Object(m.a)(Object(m.a)(Object(m.a)({},me),i?he:{}),l?pe:{}),r?fe:{})}),[i,r,l]);return o.a.createElement("div",{className:"container"},o.a.createElement("div",a({style:c}),o.a.createElement("input",s()),o.a.createElement("p",null,"Drag 'n' drop some files here, or click to select files")))}var ve=function(e){Object(u.a)(a,e);var t=Object(d.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).keyMap={SPACE:"space",ENTER:"enter",SEQUENCER:"s"},n.particles_config={num:[4,7],rps:.1,radius:[5,40],life:[1.5,3],v:[2,3],tha:[-40,40],alpha:[.6,0],scale:[1,.1],position:"center",color:["random","#ff0000"],cross:"dead",random:15,g:5,onParticleUpdate:function(e,t){e.beginPath(),e.rect(t.p.x,t.p.y,2*t.radius,2*t.radius),e.fillStyle=t.color,e.fill(),e.closePath()}},n.loadingTextArray=["Loading your Model...","This may take a while...","You look good today!","Did you drink enough water?","It's not you. It's me.","Help, I'm trapped in a loader!","Counting backwards from Infinity","Don't Panic"],n.storeDropContent=function(e){var t=new FileReader;t.readAsDataURL(e[0]);var a=Object(c.a)(n);t.onloadend=function(){var e=t.result.replace(/^data:.+;base64,/,"");a.setState({files:e}),fetch("/upload",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:e})}).then((function(e){return e.json()})).then((function(e){a.setState({isReadyForGeneration:!0,isUploadSuccessful:!0}),console.log(e.result)}))}},n.scatterMarkerClick=function(e,t,a){a.seriesIndex;var o=a.dataPointIndex;a.config;console.log(n.state.series[0].data[o].sound);var s=n.state.series[0].data[o].sound;n.setState({selectedPoint:s})},n.onGenerate=function(e){n.setState({isLoading:!0}),fetch("/generate",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:n.state.files?n.state.files:"generated.wav",model:n.state.model,model_instrument:n.state.model_instrument,selectedPoint:n.state.selectedPoint,ae_variance:n.state.ae_variance,timestamp:(new Date).getTime()})}).then((function(e){return e.json()})).then((function(e){var t=new Audio("data:audio/wav;base64,"+e.result);n.setState({result:e.result,sound:t,processedSound:t,isLoading:!1,isReadyForPostprocessing:!0,particlesColor:n.changeParticlesColor()}),t.play(),n.handleVisualization(),n.getHistoryList()}))},n.downloadStuff=function(){if(n.state.result){console.log(n.state.result);new Audio("data:audio/wav;base64,"+n.state.result);for(var e=atob(n.state.result),t=new Array(e.length),a=0;a<e.length;a++)t[a]=e.charCodeAt(a);var o=new Uint8Array(t),s=new Blob([o],{type:"audio/wav"}),i=document.createElement("a");i.href=URL.createObjectURL(s),i.download="sound.wav",document.body.appendChild(i),i.click()}else alert("Nothing to download you fool")},n.playOriginalSound=function(){fetch("/play",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:"original",model:n.state.model,model_instrument:n.state.model_instrument,selectedPoint:n.state.selectedPoint,ae_variance:n.state.ae_variance,timestamp:(new Date).getTime()})}).then((function(e){return e.json()})).then((function(e){new Audio("data:audio/wav;base64,"+e.result).play()}))},n.playStuff=function(){fetch("/play",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:n.state.files?n.state.files:"processed.wav"})}).then((function(e){return e.json()})).then((function(e){var t=new Audio("data:audio/wav;base64,"+e.result);n.setState({result:e.result,processedSound:t,isLoading:!1}),t.play(),n.handleVisualization()}))},n.handleCancelClick=function(e){n.setState({result:""})},n.handleAnotherUpload=function(e){n.setState({isReadyForGeneration:!1,isUploadSuccessful:!1,isReadyForPostprocessing:!1})},n.handleHotKeySpace=function(){console.log("Pressed Space!"),n.playStuff()},n.handleHotKeySequencer=function(){console.log("Pressed S!");var e=n.state.sequencerProps;e.startTime?(e.startTime=null,e.pastLapsedTime=0):e.startTime=performance.now(),n.setState({sequencerProps:e})},n.handleHotKeyEnter=function(){console.log("Pressed Enter!"),n.onGenerate()},n.loadSimilarityModelInBackend=function(){fetch("/similarity",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:"similarity"})}).then((function(e){return e.json()})).then((function(e){console.log(e.result),clearInterval(n.timeout),n.setState({isLoadingModel:!1,isReadyForGeneration:!0,isSimilaritySearch:!0,isUploadSuccessful:!1,isReadyForPostprocessing:!1,isReadyForGeneration:!1})}))},n.loadModelInBackend=function(e,t){fetch("/tsne",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:"tsne",model_instrument:t})}).then((function(e){return e.json()})).then((function(e){console.log(e.result),n.setState({series:e.result,isLoadingModel:!1,isReadyForGeneration:!0}),clearInterval(n.timeout)}))},n.handleDropdownVAE=function(e){console.log("VAE"),n.setState({model:"Variational Autoencoder",isGAN:!1,isSimilaritySearch:!1,isReadyForPostprocessing:!1,isReadyForGeneration:!1}),"Instrument"!==n.state.model_instrument&&(n.timeout=setInterval((function(){var e=n.state.loadingTextIdx;n.setState({loadingTextIdx:e+1})}),2500),n.setState({isLoadingModel:!0}),n.loadModelInBackend(e.target.id,n.state.model_instrument))},n.handleSimilaritySearch=function(e){console.log("Similarity Search"),n.setState({model:"Similarity Search",isGAN:!0}),n.timeout=setInterval((function(){var e=n.state.loadingTextIdx;n.setState({loadingTextIdx:e+1})}),2500),n.setState({isLoadingModel:!0}),n.loadSimilarityModelInBackend()},n.handleRandom=function(e){console.log("Random Button");var t=Math.random()<.5,a=Math.floor(101*Math.random()),o=Math.floor(101*Math.random()),s=Math.floor(101*Math.random()),i=Math.floor(101*Math.random());n.setState({distortion_value:a,reverb_value:o,highpass_value:s,lowpass_value:i,isReversed:t}),n.setState({isBookmarked:!1}),n.postEffectsUpdate(t,o,s,i,a)},n.handleDropdownInstrument=function(e){console.log(e.target),console.log(e.target.id),n.setState({model_instrument:e.target.id,isReadyForPostprocessing:!1,isReadyForGeneration:!1}),console.log(n.state.model),"Model Selection"!=n.state.model&&(n.timeout=setInterval((function(){var e=n.state.loadingTextIdx;n.setState({loadingTextIdx:e+1})}),2500),n.setState({isLoadingModel:!0}),n.loadModelInBackend(n.state.model,e.target.id))},n.handleDropdownPresets=function(e){console.log(e.target.id),fetch("/getMongoDBData",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({id:e.target.id,type:"presets"})}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({distortion_value:e.distortion_value,reverb_value:e.reverb_value,highpass_value:e.highpass_value,lowpass_value:e.lowpass_value,isReversed:e.isReversed,volume_value:e.volume_value}),n.setState({isBookmarked:!1}),n.postEffectsUpdate()}))},n.handleReverseSound=function(e){console.log("Handle Reverse"),!1===n.state.isReversed?(console.log("New State: isReversed True"),n.setState({isReversed:!0}),n.postEffectsUpdate(!0)):(console.log("New State: isReversed False"),n.setState({isReversed:!1}),n.postEffectsUpdate(!1))},n.handleVisualization=function(e){console.log("Handle Visualization"),fetch("/getVisualization",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:"visualization"})}).then((function(e){return e.json()})).then((function(e){new Audio("data:audio/wav;base64,"+e.result);n.setState({visualizations:e.visualization})}))},n.getBookmarkData=function(e){console.log("Handle History could be bookmark or history"),console.log(e.target.id),console.log(e),fetch("/getMongoDBData",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({id:e.target.id,type:"bookmark"})}).then((function(e){return e.json()})).then((function(e){var t=new Audio("data:audio/wav;base64,"+e.result);n.setState({distortion_value:e.distortion_value,reverb_value:e.reverb_value,highpass_value:e.highpass_value,lowpass_value:e.lowpass_value,isReversed:e.isReversed,volume_value:e.volume_value,result:e.result,processedSound:t,isLoading:!1}),t.play(),n.setState({isBookmarked:!1}),n.postEffectsUpdate()}))},n.getHistoryData=function(e){fetch("/getMongoDBData",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({id:e.target.id,type:"history"})}).then((function(e){return e.json()})).then((function(e){console.log(e);var t=new Audio("data:audio/wav;base64,"+e.result);n.setState({result:e.result,processedSound:t,isLoading:!1}),t.play(),console.log("Hat er nicht abgespielt? Das w\xe4re doof."),n.handleVisualization()}))},n.handleBookmark=function(e){console.log("Bookmark"),!1===n.state.isBookmarked?(console.log("New State: Bookmarked"),fetch("/bookmark",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:"Bookmark_value",volume_value:n.state.volume_value,distortion_value:n.state.distortion_value,reverb_value:n.state.reverb_value,highpass_value:n.state.highpass_value,lowpass_value:n.state.lowpass_value,isReversed:n.state.isReversed,model:n.state.model,model_instrument:n.state.model_instrument,timestamp:(new Date).getTime()})}).then((function(e){return e.json()})).then((function(e){console.log("successfully wrote bookmark to database")})),n.setState({isBookmarked:!0}),n.getBookmarksList()):(console.log("New State: Not Bookmarked"),n.setState({isBookmarked:!1}))},n.handleScatterClick=function(e){console.log("Scatter"),console.log(e)},n.changeParticlesColor=function(){var e=["#0000ff","#ff00ff","#ff0000","#00ffff","#00ff00"];return e[Math.floor(Math.random()*e.length)]},n.getBookmarksList=function(){fetch("/getMongoDBList",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({type:"bookmarks"})}).then((function(e){return e.json()})).then((function(e){console.log(e);var t=e.result;t.sort((function(e,t){return t.timestamp-e.timestamp})),n.setState({bookmarks:t})}))},n.getHistoryList=function(){fetch("/getMongoDBList",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({type:"history"})}).then((function(e){return e.json()})).then((function(e){console.log(e);var t=e.result;t.sort((function(e,t){return t.timestamp-e.timestamp})),n.setState({history:t})}))},n.handleOnChange=function(e,t){"distortion"===t&&(console.log("The Target Distortion Amount is"+n.state.distortion_value),n.setState({distortion_value:e})),"reverb"===t&&(console.log("The Target Reverb Amount is"+n.state.reverb_value),n.setState({reverb_value:e})),"volume"===t&&(console.log("The Target Volume Amount is"+n.state.volume_value),n.setState({volume_value:e})),"lowpass"===t&&(console.log("The Target lowpass amount is"+n.state.lowpass_value),n.setState({lowpass_value:e})),"highpass"===t&&(console.log("The Target highpass Amount is"+n.state.highpass_value),n.setState({highpass_value:e}))},n.postEffectsUpdate=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:null,o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:null,s=arguments.length>4&&void 0!==arguments[4]?arguments[4]:null,i=arguments.length>5&&void 0!==arguments[5]?arguments[5]:null;null===e&&(e=n.state.isReversed),null===t&&(t=n.state.volume_value),null===i&&(i=n.state.distortion_value),null===a&&(a=n.state.reverb_value),null===o&&(o=n.state.highpass_value),null===s&&(s=n.state.lowpass_value),console.log("is Reversed Value bei PostEffectsUpdate"),console.log(e),fetch("/effects",{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify({data:"Effect_Values",volume_value:t,distortion_value:i,reverb_value:a,highpass_value:o,lowpass_value:s,isReversed:e})}).then((function(e){return e.json()})).then((function(e){console.log("successfully generated Processed.wav file")}))},n.handleChangeComplete=function(e,t){"distortion"===t&&console.log("The Target Distortion Amount is"+n.state.distortion_value),"reverb"===t&&console.log("The Target Reverb Amount is"+n.state.reverb_value),"volume"===t&&console.log("The Target Volume Amount is"+n.state.volume_value),"lowpass"===t&&console.log("The Target Lowpass Amount is"+n.state.lowpass_value),"highpass"===t&&console.log("The Target Highpass Amount is"+n.state.highpass_value),n.postEffectsUpdate(),n.setState({isBookmarked:!1})},n.setStartTime=function(e){var t=n.state.sequencerProps;t.startTime=e,n.setState({sequencerProps:t})},n.handleChangeAEVariance=function(e){n.setState({ae_variance:e.target.value}),console.log(e.target.value)},n.setPastLapse=function(e){var t=n.state.sequencerProps;t.pastLapse=e,n.setState({sequencerProps:t})},n.setBPM=function(e){var t=n.state.sequencerProps;t.setBPM=e,n.setState({sequencerProps:t})},n.myRef=o.a.createRef(),n.state={isLoading:!1,isGAN:!0,isLoadingModel:!1,isReadyForGeneration:!1,isReadyForPostprocessing:!1,loadingTextIdx:0,isAE:!1,isDDSP:!1,isBookmarked:!1,isSimilaritySearch:!1,isUploadSuccessful:!1,bookmarks:[],history:[],playing:!1,isReversed:!1,model:"Model Selection",model_instrument:"Instrument",result:"idd",selectedPoint:null,visualizations:null,files:"",sound:null,processedSound:null,volumeSliderValue:100,distortion_value:0,particlesColor:"#a9a9a9",reverb_value:0,volume_value:100,lowpass_value:100,highpass_value:0,ae_variance:0,sequencerProps:{startTime:null,pastLapsedTime:0,BPM:120,setBPM:120,currentStepID:null,totalSteps:16},series:[{name:"Autoencoder Claps",data:[{x:34.7574,y:37.994343,sound:"clap2"},{x:-31.031717,y:10.498918,sound:"clap3"}]}],options:{chart:{toolbar:{show:!1},type:"scatter",zoom:{enabled:!0,type:"xy"},events:{markerClick:n.scatterMarkerClick}},xaxis:{tickAmount:10,labels:{show:!1,formatter:function(e){return parseFloat(e).toFixed(1)}}},yaxis:{show:!1,tickAmount:7}}},n}return Object(r.a)(a,[{key:"componentDidMount",value:function(){this.getBookmarksList(),this.getHistoryList()}},{key:"render",value:function(){var e=this,t=this.state.isLoading,a=this.state.isBookmarked?"dark":"success",n=this.state.isBookmarked?"Bookmarked \u2b50":"Bookmark",s=this.state.isReversed?"secondary":"success",i=this.state.isReversed?"Undo Reverse":"Reverse Sound",l=this.loadingTextArray[this.state.loadingTextIdx%this.loadingTextArray.length];return o.a.createElement(p.a,null,o.a.createElement(S.GlobalHotKeys,{keyMap:this.keyMap,handlers:{SPACE:this.handleHotKeySpace,SEQUENCER:this.handleHotKeySequencer,ENTER:this.handleHotKeyEnter}}),o.a.createElement("div",{className:"content"},o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement("h2",null,"Select your Model and Instrument"))),o.a.createElement("img",{src:re,className:"ribbon"}),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement(b.a,null,o.a.createElement(b.a.Toggle,{block:!0,variant:"primary",id:"dropdown-basic"},this.state.model),o.a.createElement(b.a.Menu,{align:"right"},o.a.createElement(b.a.Item,{onClick:this.handleDropdownVAE},"Variational Autoencoder"),o.a.createElement(b.a.Item,{onClick:this.handleSimilaritySearch},"Similarity Search")))),this.state.isSimilaritySearch?o.a.createElement("div",null):o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement(b.a,null,o.a.createElement(b.a.Toggle,{block:!0,variant:"primary",id:"dropdown-basic"},this.state.model_instrument),o.a.createElement(b.a.Menu,null,o.a.createElement(b.a.Item,{id:"Kick",onClick:this.handleDropdownInstrument},"Kick"),o.a.createElement(b.a.Item,{id:"Snare",onClick:this.handleDropdownInstrument},"Snare"),o.a.createElement(b.a.Item,{id:"Hihat",onClick:this.handleDropdownInstrument},"Hi-Hat"),o.a.createElement(b.a.Item,{id:"Clap",onClick:this.handleDropdownInstrument},"Clap"),o.a.createElement(b.a.Item,{id:"Crash",onClick:this.handleDropdownInstrument},"Crash"),o.a.createElement(b.a.Item,{id:"Ride",onClick:this.handleDropdownInstrument},"Ride"),o.a.createElement(b.a.Item,{id:"Conga",onClick:this.handleDropdownInstrument},"Conga"),o.a.createElement(b.a.Item,{id:"Cowbell",onClick:this.handleDropdownInstrument},"Cowbell"),o.a.createElement(b.a.Item,{id:"Rimshot",onClick:this.handleDropdownInstrument},"Rimshot"),o.a.createElement(b.a.Item,{id:"Toms",onClick:this.handleDropdownInstrument},"Toms"))))),o.a.createElement(le.a,{color:this.state.particlesColor,type:"cobweb",bg:!0,num:30}),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"fennekcol"},this.state.isSimilaritySearch?o.a.createElement(o.a.Fragment,null,o.a.createElement("h2",null,"Add your Input"),this.state.isUploadSuccessful?o.a.createElement(o.a.Fragment,null,o.a.createElement("p",null,"Your Upload was successful! Go ahead and generate your file"),o.a.createElement(g.a,{variant:"primary",onClick:this.handleAnotherUpload},"Upload Another File")):o.a.createElement(ge,{onDrop:this.storeDropContent},(function(e){var t=e.getRootProps,a=e.getInputProps;return o.a.createElement("section",null,o.a.createElement("div",t(),o.a.createElement("input",a()),o.a.createElement("p",null,"Drag 'n' drop some files here, or click to select files")))}))):o.a.createElement("div",null))),this.state.isLoadingModel?o.a.createElement("div",{align:"center"},o.a.createElement("p",null,l),o.a.createElement("div",{class:"spinner-border text-primary",role:"status"},o.a.createElement("span",{class:"sr-only"},"Loading..."))):o.a.createElement("div",null),this.state.isReadyForGeneration?o.a.createElement(o.a.Fragment,null,o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement(h.a,{className:"fennekcol"},this.state.isGAN?o.a.createElement("div",null):o.a.createElement(o.a.Fragment,null,o.a.createElement("div",{align:"center",width:"80%"},o.a.createElement(de.a,{options:this.state.options,series:this.state.series,dataPointSelection:this.handleScatterClick,type:"scatter",width:"600"}),o.a.createElement("p",null,"Variance"),o.a.createElement("input",{id:"typeinp",type:"range",min:"0",max:"5",value:this.state.ae_variance,onChange:this.handleChangeAEVariance,step:"1"})),o.a.createElement("div",{align:"center"},o.a.createElement(g.a,{variant:"primary",onClick:this.playOriginalSound},"Listen to Original Sound"))))),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement("hr",null),o.a.createElement("h2",null,"Generate your Sound"),o.a.createElement("p",{class:"text-secondary"},"Hotkeys: 'Enter' to generate, 'Space' to Play  and 's' to Sequence Sound "),o.a.createElement(g.a,{block:!0,variant:"primary",disabled:t,onClick:t?null:this.onGenerate},t?"Generating...":"Generate Sound with AI"))),o.a.createElement(f.a,{style:{marginTop:"-10px"},className:"justify-content-md-center row"},o.a.createElement(se.a,{style:{"text-align":"center"}},o.a.createElement(se.a.Toggle,{as:g.a,variant:"link",eventKey:"0"},"Show Generation History"),o.a.createElement(se.a.Collapse,{eventKey:"0"},o.a.createElement(f.a,null,o.a.createElement("div",{class:"col-12"},o.a.createElement("ul",{class:"list-group"},this.state.history.map((function(t){return o.a.createElement("li",{id:t._id,class:"list-group-item py-1 list-group-item-action",onClick:e.getHistoryData},t.instrument,o.a.createElement(k.a,{variant:"warning",style:{"margin-left":"20px"}},t.model),o.a.createElement(k.a,{variant:"danger",style:{"margin-left":"20px"}},ae(t.timestamp)))}))))))))):o.a.createElement("div",null),this.state.isReadyForPostprocessing?o.a.createElement(o.a.Fragment,null,o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement("hr",null),o.a.createElement("h2",null,"Postprocessing")),o.a.createElement(f.a,{className:"justify-content-md-center row"},this.state.result?o.a.createElement("div",null,o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(g.a,{block:!0,variant:"success",onClick:this.playStuff},this.state.playing?"Playing...":"\u25b6"))),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(E,{value:this.state.distortion_value,effect:"distortion",sound:this.state.sound,handleOnChange:this.handleOnChange,handleChangeComplete:this.handleChangeComplete,orientation:"horizontal"}),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement("p",null," Distortion "))),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(E,{value:this.state.reverb_value,effect:"reverb",sound:this.state.sound,handleOnChange:this.handleOnChange,handleChangeComplete:this.handleChangeComplete,orientation:"horizontal"}),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement("p",null," Reverb "))),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(E,{value:this.state.volume_value,effect:"volume",sound:this.state.sound,handleOnChange:this.handleOnChange,handleChangeComplete:this.handleChangeComplete,orientation:"horizontal"}),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement("p",null," Volume "))),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(E,{value:this.state.lowpass_value,effect:"lowpass",sound:this.state.sound,handleOnChange:this.handleOnChange,handleChangeComplete:this.handleChangeComplete,orientation:"horizontal"}),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement("p",null," Lowpass "))),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(E,{value:this.state.highpass_value,effect:"highpass",sound:this.state.sound,handleOnChange:this.handleOnChange,handleChangeComplete:this.handleChangeComplete,orientation:"horizontal"}),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement("p",null," Highpass ")))),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(g.a,{variant:"success",onClick:this.handleRandom},"Random \ud83c\udfb2")),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(g.a,{variant:s,onClick:this.handleReverseSound},i)),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(b.a,null,o.a.createElement(b.a.Toggle,{variant:"success",id:"dropdown-basic"},"Presets"),o.a.createElement(b.a.Menu,null,o.a.createElement(b.a.Item,{id:"Big Room",onClick:this.handleDropdownPresets},"Big Room"),o.a.createElement(b.a.Item,{id:"Small Room",onClick:this.handleDropdownPresets},"Small Room"),o.a.createElement(b.a.Item,{id:"Clipping",onClick:this.handleDropdownPresets},"Clipping")))),o.a.createElement(h.a,{className:"effectcol"},o.a.createElement(g.a,{variant:a,onClick:this.handleBookmark},n)))):o.a.createElement("div",null)),o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement("p",{class:"text-secondary"},"Your bookmarked sounds")),o.a.createElement(f.a,null,o.a.createElement("div",{class:"col-12"},o.a.createElement("ul",{class:"list-group"},this.state.bookmarks.map((function(t){return o.a.createElement("li",{id:t._id,class:"list-group-item list-group-item-action",onClick:e.getBookmarkData},t.instrument,o.a.createElement(k.a,{variant:"warning",style:{"margin-left":"20px"}},t.model),o.a.createElement(k.a,{variant:"danger",style:{"margin-left":"20px"}},ae(t.timestamp)))}))))),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement("hr",null),o.a.createElement("h2",null,"Sound Visualizer"),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement(g.a,{className:"justify-content-md-center",class:"border border-primary",variant:"light",onClick:this.handleVisualization},o.a.createElement("img",{src:ce}))))),o.a.createElement(f.a,null,o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement(ie,{visualizations:this.state.visualizations}))),this.state.result&&"i"!==this.state.result?o.a.createElement(o.a.Fragment,null,o.a.createElement(f.a,{style:{"margin-top":"30px"}},o.a.createElement(h.a,{className:"fennekcol"},o.a.createElement("hr",null),o.a.createElement("h2",null,"Sequencer"),o.a.createElement(te,{startTime:this.state.sequencerProps.startTime,pastLapsedTime:this.state.sequencerProps.pastLapsedTime,BPM:this.state.sequencerProps.setBPM,base64Sound:this.state.result,setStartTime:this.setStartTime,setPastLapse:this.setPastLapse,setBPM:this.setBPM}))),o.a.createElement(f.a,{className:"justify-content-md-center row"},o.a.createElement(g.a,{variant:"primary",onClick:this.downloadStuff},"Download"))):null):o.a.createElement("div",null)))}}]),a}(o.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(59);i.a.render(o.a.createElement(ve,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[95,1,2]]]);
//# sourceMappingURL=main.0201f51d.chunk.js.map